# Лекция 2 - Введение в Hadoop

## Особенности Hadoop

- Горизонтальное масштабирование
- Пары ключ/значение вместо реляционных таблиц
- Функциональное программирование (MapReduce) вместо декларативных запросов (SQL)
- Автономная пакетная обработка вместо оперативных транзакций

---

- Mở rộng theo chiều ngang ngang
- Cặp khóa/giá trị thay vì bảng quan hệ
- Lập trình chức năng (MapReduce) thay vì truy vấn khai báo (SQL)
- Xử lý hàng loạt ngoại tuyến thay vì giao dịch trực tuyến

---

## Архитектура HDFS

* **NameNode** — управляющий узел, узел имен
* **DataNode** — узел или сервер данных
* **Сlient** — клиент
* **Secondary NameNode** — вторичный узел имен

---

* **NameNode** — control node, namenode
* **DataNode** — node hoặc máy chủ dữ liệu
* **Khách hàng** - client
* **Node tên phụ** - namenode phụ

```{figure} hadoop-ecosystem.jpg
```

Các thành phần từ thấp lên cao:

1. **HDFS** (распределенная файловая система) - hệ thống phân tán file $\Rightarrow$ системный уровень хранения данных.
2. **YARN** (планировщик распределенной обработки данных, управление ресурсами) - bộ lập lịch xử lý dữ liệu phân tán.
3. Ba thành phần:
    * **MapReduce** (движок выполнения задач MapReduce) - công cụ thực hiện tasks;
    * **Spark** (движок распределенной обработки данных) - công cụ xử lý dữ liệu phân tán;
    * **Impala** (Low-latency SQL запросы) - truy vấn SQL với độ trễ thấp.

YARN và MapReduce/Spark hợp thành phần **Hbase** (колоночная база данных).

4. Ba thành phần:
    * **Sqoop** (загрузка данных) - tải dữ liệu;
    * **Pig** (скрипты MapReduce) - các đoạn script MapReduce;
    * **Hive** (SQL запросы) - truy vấn SQL (cho phép chạy SQL trên NoSQL) $\Rightarrow$ HỌC.
5. Oozie (оркестровка задач) - điều phối task.
6. Hue (единый веб-интерфейс для всех инструментов) - giao diện web.

### Архитектура HDFS: NameNode

* ведет учет разбиению файлов на блоки, хранит информацию о том, на каких узлах эти
блоки находятся, и следит за общим состоянием распределенной файловой
системы
* отвечает за открытие и закрытие файлов, создание и удаление каталогов, управление доступом со стороны внешних клиентов и соответствие между файлами и блоками, дублированными (реплицированными) на узлах данных

---

* lưu giữ hồ sơ về việc phân chia tệp thành các khối, lưu trữ thông tin về các nút này nằm trên các nút nào
các khối được định vị và theo dõi trạng thái chung của tệp được phân phối
hệ thống
* Chịu trách nhiệm mở và đóng tệp, tạo và xóa thư mục, quản lý quyền truy cập từ máy khách bên ngoài và ánh xạ giữa các tệp và khối trùng lặp (sao chép) trên các nút dữ liệu

```{figure} HDFS-architecture.jpg
```

### Архитектура HDFS: DataNode

* отвечает за запись и чтение данных
* данные хранятся в блоках, объем которых можно задавать при настройке кластера
* выполняет команды от узла NameNode по созданию, удалению и репликации блоков
* периодически отправляет сообщения о состоянии (heartbeats)
* обрабатывает запросы на чтение и запись, поступающих от клиентов файловой системы HDFS.

---

* chịu trách nhiệm ghi và đọc dữ liệu
* dữ liệu được lưu trữ theo khối, khối lượng có thể được đặt khi thiết lập cluster
* thực thi các lệnh từ NameNode để tạo, xóa và sao chép các khối
* gửi thông báo trạng thái định kỳ (nhịp tim)
* xử lý các yêu cầu đọc và ghi từ các máy khách hệ thống tệp HDFS.

```{figure} HDFS-example.jpg
```

### Архитектура HDFS: Secondary NameNode

**Secondary NameNode** — вторичный узел имен, отдельный сервер, единственный в кластере, который копирует образ HDFS и лог транзакций операций с файловыми блоками во временную папку, применяет изменения, накопленные в логе транзакций к образу HDFS, а также записывает его на узел NameNode и очищает лог транзакций.

**NameNode phụ** - nút tên phụ, máy chủ riêng biệt, máy chủ duy nhất trong cluster sao chép hình ảnh HDFS và nhật ký giao dịch của các hoạt động với các khối tệp vào một thư mục tạm thời, áp dụng các thay đổi được tích lũy trong nhật ký giao dịch vào hình ảnh HDFS, đồng thời ghi nó vào nút NameNode và xóa nhật ký giao dịch.

Secondary NameNode необходим для быстрого ручного восстановление NameNode в случае его выхода из строя.

NameNode phụ là cần thiết để khôi phục thủ công nhanh chóng NameNode trong trường hợp nó bị lỗi.

```{figure} HDFS-second-namenode.jpg
```

## Знакомство с MapReduce

**MapReduce** - модель распределённых вычислений для параллельной обработки больших объёмов информации.

* **Map** – распределение
* **Shuffle** – перераспределение
* **Reduce** – редукция

**MapReduce** là mô hình điện toán phân tán để xử lý song song lượng lớn thông tin.

* **Map** – phân bổ
* **Shuffle** – phân phối lại
* **Reduce** – giảm

```{figure} MapReduce-intro.jpg
```

### MapReduce: шаг Map

На шаге Map происходит предварительная обработка данных - главный узел кластера (master node) получает набор данных, делит его на части и передает рабочим узлам (worker node).

Ở bước Map, dữ liệu được xử lý trước - nút chính của cluster (master node) nhận tập dữ liệu, chia thành các phần và chuyển nó đến các nút làm việc (worker node).

Каждый рабочий узел применяет функцию Map к локальным данным и записывает результат в формате «ключ-значение» во временное хранилище.

Mỗi nút làm việc áp dụng chức năng Map cho dữ liệu cục bộ và ghi kết quả ở định dạng khóa-giá trị vào bộ lưu trữ tạm thời.

```{figure} MapReduce-map.jpg
```

### MapReduce: шаг Shuffle

```{figure} MapReduce-shuffle.jpg
```

### MapReduce: шаг Reduce

```{figure} MapReduce-reduce.jpg
```

### Ví dụ sử dụng MapReduce

```{figure} MapReduce-example.jpg
```

## Реализация в Hadoop

**JobTraker** - строит план выполнения, то есть определяет, какие файлы обрабатывать, назначает узлы различным задачам и следит за ходом исполнения этих задач. В кластере Hadoop может быть только один демон JobTracker.

**JobTracker** - xây dựng kế hoạch thực hiện, tức là xác định tệp nào sẽ xử lý, gán nút cho các tác vụ khác nhau và theo dõi tiến trình của các tác vụ này. Chỉ có thể có một daemon JobTracker trong cluster Hadoop.

TaskTraker - управляют исполнением отдельных заданий на подчиненных узлах.

TaskTraker - quản lý việc thực hiện các tác vụ riêng lẻ trên các nút slave.

## Преимущества применения MapReduce

**возможность распределенного выполнения операций** предварительной обработки (map) и свертки (reduce) большого объема данных. При этом функции map работают независимо друг от друга и могут выполняться параллельно на разных узлах кластера. 

**быстрота обработки больших объёмов данных** за счет распределения операций (сортировка петабайта данных при использовании MapReduce за пару часов)

**отказоустойчивость и оперативное восстановления после сбоев**: при отказе рабочего узла, производящего операцию map или reduce, его работа автоматически передается другому рабочему узлу в случае доступности входных данных для проводимой операции.

---

**khả năng thực hiện các hoạt động phân tán** tiền xử lý (bản đồ) và giảm (giảm) lượng lớn dữ liệu. Trong trường hợp này, các hàm bản đồ hoạt động độc lập với nhau và có thể được thực thi song song trên các nút cụm khác nhau.

**xử lý nhanh khối lượng dữ liệu lớn** do phân phối hoạt động (sắp xếp một petabyte dữ liệu bằng MapReduce trong vài giờ)

**Khả năng chịu lỗi và phục hồi nhanh chóng sau các lỗi**: nếu nút công nhân thực hiện thao tác ánh xạ hoặc rút gọn không thành công, công việc của nó sẽ tự động được chuyển sang nút công nhân khác nếu có sẵn dữ liệu đầu vào cho thao tác.

## Недостатки MapReduce

**недостаточно высокая производительность** – классическая технология, в частности, реализованная в ядре Apache Hadoop, обрабатывает данные ациклично в пакетном режиме. При этом функции Reduce не запустятся до завершения всех процессов Map. Все операции проходят по циклу чтение-запись с жесткого диска, что влечет задержки (latency) в обработке информации.

**ограниченность применения** – высокие задержки распределенных вычислений, приемлемые в пакетном режиме обработки, не позволяют использовать классический MapReduce для потоковой обработки в режиме реального времени, повторяющихся запросов и итеративных алгоритмов на одном и том же датасете, как в задачах машинного обучения.

---

**hiệu suất không đủ cao** – công nghệ cổ điển, đặc biệt, được triển khai trong nhân Apache Hadoop, xử lý dữ liệu theo chu kỳ ở chế độ hàng loạt. Trong trường hợp này, chức năng Reduce sẽ không bắt đầu cho đến khi tất cả quá trình Map hoàn tất. Mọi thao tác đều trải qua chu trình đọc-ghi từ ổ cứng, kéo theo độ trễ (latency) trong quá trình xử lý thông tin.

**ứng dụng hạn chế** - độ trễ cao của điện toán phân tán, có thể chấp nhận được ở chế độ xử lý hàng loạt, không cho phép sử dụng MapReduce cổ điển để xử lý phát trực tuyến theo thời gian thực, các truy vấn lặp lại và thuật toán lặp trên cùng một tập dữ liệu, như trong các vấn đề về học máy.

## Часть 2. Основы SQL

**Соединение (JOIN)** - операция для сопоставления строки одной таблицы строкам другой таблицы.

Синтаксис

```{code-block} sql
SELECT * FROM
TableA a INNER join TableB b
ON
a.name=b.name;
```

### Виды JOIN

* INNER JOIN
* LEFT JOIN
* RIGHT JOIN
* FULL JOIN
