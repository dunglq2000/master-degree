# Лекция 3. Apache Spark: Часть 1

## Недостатки применения MapReduce

> Nhược điểm khi sử dụng MapReduce

Хотя Apache Hadoop получил широкое распространение, платформа MapReduce для HDFS имела несколько недостатков

- трудно управлять и администрировать;
- общий API пакетной обработки MapReduce очень подробный и требует большого количества шаблонного кода настройки, имеющей низкую отказоустойчивость;
- при выполнении множества пар задач MapReduce на больших объемах данных, промежуточный результат каждой пары записывается на локальный диск для последующего этапа его выполнения.
- не подходит для таких видов задач, как задачи машинного обучения, потоковой передачи, интерактивных SQL-запросов.

Mặc dù Apache Hadoop đã được áp dụng rộng rãi nhưng nền tảng MapReduce cho HDFS có một số nhược điểm

- Khó quản lý và điều hành;
- API xử lý hàng loạt MapReduce nói chung rất chi tiết và yêu cầu nhiều mã cấu hình soạn sẵn, có khả năng chịu lỗi thấp;
- khi thực hiện nhiều cặp tác vụ MapReduce trên lượng lớn dữ liệu, kết quả trung gian của mỗi cặp sẽ được ghi vào đĩa cục bộ cho giai đoạn thực hiện tiếp theo.
- không phù hợp với các loại tác vụ như tác vụ học máy, phát trực tuyến, truy vấn SQL tương tác.

$\Rightarrow$ инженеры разработали индивидуальные системы (Apache Hive, Apache Storm, Apache Impala и т. д.), с индивидуальным API и конфигурациями кластеров, что еще больше усложняет работу Hadoop и усложняет 
процесс обучения для разработчиков

$\Rightarrow$ Các kỹ sư đã phát triển các hệ thống tùy chỉnh (Apache Hive, Apache Storm, Apache Impala, v.v.), với các API tùy chỉnh và cấu hình cụm, thậm chí còn tăng thêm độ phức tạp cho Hadoop và
quá trình học tập cho các nhà phát triển

## Создание Apache Spark

> Tạo Apache Spark

Есть ли способ сделать Hadoop и MapReduce проще и быстрее?

$\Rightarrow$ Исследователи из Калифорнийского университета решили эту задачу с помощью проекта, который они назвали Spark. Основной целью проекта Spark было внедрение идей из Hadoop MapReduce c улучшениями:

- быть очень отказоустойчивой;
- поддерживать хранение в памяти промежуточных результатов вычислений;
- предлагать простые и составныеAPI на нескольких языках программирования.

Có cách nào để làm cho Hadoop và MapReduce dễ dàng hơn và nhanh hơn không?

$\Rightarrow$ Các nhà nghiên cứu tại Đại học California đã giải quyết vấn đề này bằng một dự án mà họ gọi là Spark. Mục tiêu chính của dự án Spark là triển khai các ý tưởng từ Hadoop MapReduce với những cải tiến:

- rất có khả năng chịu lỗi;
- hỗ trợ lưu trữ kết quả tính toán trung gian vào bộ nhớ;
- cung cấp các API đơn giản và phức tạp bằng nhiều ngôn ngữ lập trình.

## Ключевые характеристики Apache Spark

> Các tính năng chính của Apache Spark

- **скорость** - в Spark высокая скорость обработки данных достигается несколькими способами. Во-первых, внутренняя реализация Spark значительно выигрывает от недавних огромных успехов индустрии аппаратного обеспечения по части повышения производительности процессоров и памяти. Во вторых, планировщик Spark и оптимизатор запросов Catalyst создает эффективный план вычислений, который можно разложить на параллельно выполняемые задачи. Благодаря тому, что все промежуточные результаты сохраняются в памяти и для них нет дискового ввода-вывода, значительно повышается производительность всех вычислений.
- **tốc độ** - trong Spark, tốc độ xử lý dữ liệu cao đạt được theo nhiều cách. Đầu tiên, việc triển khai nội bộ của Spark được hưởng lợi rất nhiều từ những bước tiến lớn gần đây của ngành phần cứng trong việc cải thiện hiệu suất bộ xử lý và bộ nhớ. Thứ hai, bộ lập lịch Spark và trình tối ưu hóa truy vấn Catalyst tạo ra một kế hoạch tính toán hiệu quả có thể được phân tách thành các tác vụ song song. Do thực tế là tất cả các kết quả trung gian đều được lưu trữ trong bộ nhớ và không có I/O đĩa cho chúng nên hiệu suất của tất cả các phép tính được cải thiện đáng kể.
- **простота использования** — Spark предоставляет фундаментальную абстракцию логической структуры данных, называемой устойчивым распределенным набором данных (анг. Resilient Distributed Dataset, RDD), на основе которой строятся все другие абстракции структурированных данных более высокого уровня, такие как фреймы данных (DataFrame) и наборы данных (DataSets). Предоставляя набор преобразований и действий в виде операций, Spark предлагает простую модель программирования, которую можно использовать с целью создания приложений для обработки больших данных на знакомых языках программирования.
- **dễ sử dụng** - Spark cung cấp sự trừu tượng hóa cơ bản của cấu trúc dữ liệu logic, được gọi là Tập dữ liệu phân tán linh hoạt (RDD), trên đó tất cả các trừu tượng hóa dữ liệu có cấu trúc cấp cao hơn khác, chẳng hạn như DataFrames, được xây dựng, và các tập dữ liệu (Bộ dữ liệu). Bằng cách cung cấp một tập hợp các phép biến đổi và hành động dưới dạng hoạt động, Spark cung cấp một mô hình lập trình đơn giản có thể được sử dụng để xây dựng các ứng dụng dữ liệu lớn bằng các ngôn ngữ lập trình quen thuộc.
- **модульность** - операции Spark могут применяться ко многим типам рабочих нагрузок и выражаться на любом из поддерживаемых языков программирования: Scala, Java, Python, SQL и R. Spark предлагает унифицированные библиотеки с хорошо документированными API-интерфейсами.
- **tính mô-đun** - Hoạt động của Spark có thể được áp dụng cho nhiều loại khối lượng công việc và được thể hiện bằng bất kỳ ngôn ngữ lập trình nào được hỗ trợ: Scala, Java, Python, SQL và R. Spark cung cấp các thư viện hợp nhất với các API được ghi chép rõ ràng.
- **расширяемость** - Spark фокусируется на своем быстром механизме параллельных вычислений, а не на хранилище. В отличии от Apache Hadoop, который включает в себя как хранилище, так и вычисления, в Spark происходит их разделение. Это означает, что можно использовать Spark для чтения данных, хранящихся в множестве источников.
- **khả năng mở rộng** - Spark tập trung vào công cụ tính toán song song nhanh hơn là lưu trữ. Không giống như Apache Hadoop, bao gồm cả lưu trữ và tính toán, Spark tách chúng ra. Điều này có nghĩa là bạn có thể sử dụng Spark để đọc dữ liệu được lưu trữ ở nhiều nguồn.

## Модули Apache Spark

```{figure} modules-apache-spark.png
```

## Модуль Spark SQL

**Модуль Spark SQL** предназначен для работы со структурированными данными. Он позволяет считывать данные, хранящиеся в таблице СУБД, или из форматов файлов со структурированными данными (CSV, txt, JSON, Parquet и т.д.), а затем создавать постоянные или временные таблицы в Spark. Кроме того, при использовании структурированных API-интерфейсов Spark на Java, Python, Scala или R можно комбинировать SQL-подобные запросы для запроса данных, только что считанных в фрейм данных Spark. На сегодняшний день Spark SQLявляетсяANSI SQL: 2003 [34] функционирует как чистый SQL-движок.

**Mô-đun Spark SQL** được thiết kế để hoạt động với dữ liệu có cấu trúc. Nó cho phép bạn đọc dữ liệu được lưu trữ trong bảng DBMS hoặc từ các định dạng tệp dữ liệu có cấu trúc (CSV, txt, JSON, Parquet, v.v.) và sau đó tạo các bảng cố định hoặc tạm thời trong Spark. Ngoài ra, khi bạn sử dụng API có cấu trúc của Spark trong Java, Python, Scala hoặc R, bạn có thể kết hợp các truy vấn giống SQL để truy vấn dữ liệu vừa đọc vào khung dữ liệu Spark. Ngày nay Spark SQL là ANSI SQL: 2003 [34] hoạt động như một công cụ SQL thuần túy.

## Модуль Spark MLlib
 
**Модуль Spark MLlib** является библиотекой, содержащей общие алгоритмы машинного обучения. MLlib предоставляет множество популярных алгоритмов машинного обучения, построенных поверх API на основе фреймов данных высокого уровня для построения моделей. Эти API позволяют извлекать или преобразовывать функции, создавать конвейеры (для обучения и оценки) и сохранять модели (для их сохранения и перезагрузки) во время развертывания. Дополнительные утилиты включают использование общих операций линейной алгебры и статистики. MLlib включает в себя другие низкоуровневые примитивы машинного обучения, включая общую оптимизацию градиентного спуска.

**Mô-đun Spark MLlib** là thư viện chứa các thuật toán học máy phổ biến. MLlib cung cấp nhiều thuật toán học máy phổ biến được xây dựng dựa trên các API dựa trên khung dữ liệu cấp cao để xây dựng mô hình. Các API này cho phép bạn trích xuất hoặc chuyển đổi các tính năng, tạo quy trình (để đào tạo và đánh giá) cũng như duy trì các mô hình (để lưu và tải lại chúng) trong quá trình triển khai. Các tiện ích bổ sung bao gồm việc sử dụng đại số tuyến tính và thống kê tổng quát. MLlib bao gồm các nguyên tắc học máy cấp thấp khác, bao gồm tối ưu hóa giảm độ dốc chung.

## Модуль Spark Sreaming
 
**Модуль Spark Streaming** — предназначен для непрерывной потоковой передачи, предоставляет структурированные API потоковой передачи, построенные поверх SQL-движка Spark и API на основе фреймов данных. Данная модель рассматривает поток как постоянно растущую таблицу с добавлением новых строк данных в конце, что позволяет работать в режиме реального времени с потоковыми данными из таких движков, как Apache Kafka, и других потоковых источников. В рамках модели структурированной потоковой передачи ядро Spark SQL обрабатывает все аспекты отказоустойчивости и семантики поздних данных, позволяющие разработчикам сосредоточиться на написании потоковых приложений.

```{figure} module-spark-sreaming.png
```

**Spark Streaming Module** - được thiết kế để phát trực tuyến liên tục, cung cấp các API phát trực tuyến có cấu trúc được xây dựng dựa trên công cụ SQL và API dựa trên khung dữ liệu của Spark. Mô hình này xử lý luồng như một bảng ngày càng phát triển với các hàng dữ liệu mới được thêm vào cuối, cho phép làm việc trong thời gian thực với dữ liệu truyền trực tuyến từ các công cụ như Apache Kafka và các nguồn phát trực tuyến khác. Theo mô hình phát trực tuyến có cấu trúc, công cụ Spark SQL xử lý tất cả các khía cạnh về khả năng chịu lỗi và ngữ nghĩa dữ liệu trễ, cho phép các nhà phát triển tập trung vào việc viết các ứng dụng phát trực tuyến.

## Модуль GraphX
 
**Модуль GraphX** — это библиотека для работы с графами (например, графами социальных сетей, маршрутами и точками подключения или топологии сети) и выполнения параллельных вычислений на графах. Вводится новая абстракцию Graph — ориентированный мультиграф свойств, характерный для каждой вершины и ребра. Его называют граф свойств (Property Graph), элементы которого представляют собой определяемыми пользователем объектами, прикрепленные к каждой вершине и ребру. Такое распараллеливание упрощает сценарии моделирования, когда между одними и теми же вершинами может быть несколько отношений, например, коллега и друг, роль в проекте и должность в оргструктуре компании.

**Mô-đun GraphX ​​** là thư viện để làm việc với biểu đồ (ví dụ: biểu đồ mạng xã hội, tuyến đường và điểm kết nối hoặc cấu trúc liên kết mạng) và thực hiện các phép tính song song trên biểu đồ. Một biểu đồ trừu tượng mới được giới thiệu - một biểu đồ đa hướng có hướng của các thuộc tính cụ thể cho từng đỉnh và cạnh. Nó được gọi là Đồ thị thuộc tính, có các phần tử là các đối tượng do người dùng xác định được gắn vào mỗi đỉnh và cạnh. Sự song song hóa này đơn giản hóa các kịch bản mô hình hóa khi có thể có một số mối quan hệ giữa các đỉnh giống nhau, chẳng hạn như đồng nghiệp và bạn bè, một vai trò trong một dự án và một vị trí trong cơ cấu tổ chức của công ty.

## Архитектура Apache Spark

**Apache Spark** — это программное средство распределенной обработки данных компоненты которого совместно работают на кластере машин

**Apache Spark** là phần mềm xử lý dữ liệu phân tán có các thành phần hoạt động cùng nhau trên một cụm máy

**Основные компоненты**

- Приложение Spark
- Драйвер Spark
- СессияSpark
- Менеджер кластера
- Исполнитель Spark

**Thành phần chính**

- Ứng dụng tia lửa
- Trình điều khiển tia lửa
- PhiênSpark
- Người quản lý cụm
- Nghệ sĩ Spark

```{figure} architecture-apache-spark.png
```

На высоком уровне архитектуры Spark — **приложение Spark**, которое состоит из ведущего процесса, содержащего высокоуровневую логику Spark, и набора процессов исполнителей, которые могут быть разбросаны по узлам кластера. Сама программа Spark работает на узле драйвера и отправляет команды исполнителям. На одном кластере можно запустить в конкурентном режиме несколько приложений Spark.

Ở cấp độ cao của kiến ​​trúc Spark, **ứng dụng Spark** bao gồm một quy trình chính chứa logic Spark cấp cao và một tập hợp các quy trình thực thi có thể nằm rải rác trên các nút cụm. Bản thân chương trình Spark chạy trên nút trình điều khiển và gửi lệnh đến người thực thi. Bạn có thể chạy đồng thời nhiều ứng dụng Spark trên một cụm.

**Драйвер Spark** как часть приложения Spark, отвечающая за создание экземпляра сеанса Spark (SparkSession), выполняет несколько ролей:
- взаимодействует с менеджером кластера;
- запрашивает ресурсы (процессор, память и т.д.) у менеджера кластера для исполнителей Spark (JVM);
- преобразует все операции Spark в вычисления DAG, планирует их и распределяет их выполнение в виде задач между исполнителями Spark.

**Trình điều khiển Spark**, là một phần của ứng dụng Spark chịu trách nhiệm khởi tạo Phiên Spark (SparkSession), thực hiện một số vai trò:
- tương tác với người quản lý cụm;
- yêu cầu tài nguyên (CPU, bộ nhớ, v.v.) từ trình quản lý cụm cho người thực thi Spark (JVM);
- chuyển đổi tất cả các hoạt động của Spark thành các phép tính DAG, lên lịch cho chúng và phân phối việc thực thi chúng dưới dạng nhiệm vụ giữa những người thực thi Spark.

**SparkSession** является единой точкой входа для всех операций и данных Spark. С помощью этой единственной точки входа можно создавать параметры среды выполнения JVM, определять фреймы данных и наборы данных, считывать данные из источников, получать доступ к метаданным каталога и выполнять запросы Spark SQL. В автономном приложении Spark можно создать сеанс Spark с помощью одного из высокоуровневыхAPI на выбранном языке программирования.

**SparkSession** là điểm truy cập duy nhất cho tất cả hoạt động và dữ liệu của Spark. Từ điểm nhập duy nhất này, bạn có thể tạo cài đặt thời gian chạy JVM, xác định khung dữ liệu và bộ dữ liệu, đọc dữ liệu từ các nguồn, truy cập siêu dữ liệu danh mục và chạy truy vấn Spark SQL. Trong ứng dụng Spark độc lập, bạn có thể tạo phiên Spark bằng một trong các API cấp cao trong ngôn ngữ lập trình mà bạn chọn.

**Менеджер кластера** отвечает за управление и распределение ресурсов для узлов кластера, на которых выполняется приложение Spark.

**Trình quản lý cụm** chịu trách nhiệm quản lý và phân bổ tài nguyên cho các nút cụm chạy ứng dụng Spark.

В настоящее время Spark поддерживает четыре менеджера кластеров: встроенный автономный менеджер кластеров, Apache Hadoop YARN, Apache Mesos и Kubernetes. Хотя проект Spark и создавался для упрощения процесса разработки, настройка и управление кластером все же не является тривиальной задачей. Настройка всего кластера предполагает установление всех необходимых компонентов на каждом рабочем узле кластера: начиная от JVM и заканчивая библиотеками, необходимыми для корректной работы всего кластера.

Spark hiện hỗ trợ bốn trình quản lý cụm: trình quản lý cụm độc lập tích hợp sẵn, Apache Hadoop YARN, Apache Mesos và Kubernetes. Mặc dù dự án Spark được tạo ra để đơn giản hóa quá trình phát triển nhưng việc thiết lập và quản lý một cụm vẫn không phải là một nhiệm vụ tầm thường. Thiết lập toàn bộ cụm liên quan đến việc cài đặt tất cả các thành phần cần thiết trên mỗi nút làm việc của cụm: từ JVM đến các thư viện cần thiết để toàn bộ cụm hoạt động chính xác.

**Исполнитель Spark** запускается на каждом рабочем узле кластера.

**Spark executor** chạy trên mỗi nút công nhân trong cụm.

Исполнители взаимодействуют с программой драйвера и отвечают за выполнение задач. В большинстве режимов развертывания на каждом узле выполняется только один исполнитель.

Người thực thi tương tác với chương trình điều khiển và chịu trách nhiệm hoàn thành nhiệm vụ. Trong hầu hết các chế độ triển khai, chỉ có một trình thực thi chạy trên mỗi nút.

## Модель параллельных вычислений: наборы RDD

Spark представляет большие наборы данных в виде наборов RDD (Resilient Distributed Dataset) — неизменяемых, распределенных коллекций объектов, хранимых в исполнителях (ведомых узлах).

Spark biểu thị các tập dữ liệu lớn dưới dạng RDD (Bộ dữ liệu phân tán có khả năng phục hồi) — các bộ sưu tập đối tượng phân tán, không thay đổi được lưu trữ trong các bộ thực thi (nút nô lệ).

Составляющие наборы объекты называются секциями и могут вычисляться на различных узлах распределенной системы. Spark умеет хранить RDD в оперативной памяти узлов-исполнителей во время всего времени жизни приложения Spark ради ускорения доступа при повторяемых вычислениях. Наборы RDD реализованы в Spark как неизменяемые, так что преобразование объекта RDD возвращает новый объект, а не уже существующий.

Các đối tượng tạo nên các tập hợp được gọi là các phần và có thể được tính toán trên các nút khác nhau của hệ thống phân tán. Spark có thể lưu trữ RDD trong RAM của các nút thực thi trong suốt thời gian tồn tại của ứng dụng Spark để tăng tốc độ truy cập trong các phép tính lặp lại. Các bộ RDD được triển khai dưới dạng bất biến trong Spark, do đó, việc chuyển đổi một đối tượng RDD sẽ trả về một đối tượng mới thay vì đối tượng hiện có.

```{figure} RDD-set.png
```

## Отложенные вычисления

Вместо вычисления каждого преобразования сразу же после того, как его задаст драйверная программа, Spark вычисляет RDD отложенным образом, рассчитывая результат преобразований набора только при вызове действия.

Thay vì tính toán từng phép biến đổi ngay sau khi chương trình trình điều khiển chỉ định nó, Spark đánh giá RDD một cách lười biếng, chỉ tính kết quả của các phép biến đổi tập hợp khi hành động được gọi.

---

**Действие** — операция Spark, возвращающая что-либо внешней по отношению к Spark (к исполнителям Spark) системе. Примером может послужить возврат данных драйверу (такими операциями, как count или collect) или запись данных во внешнюю систему хранения. Действия вызывают срабатывание планировщика, который строит ориентированный ациклический граф (directed acyclic graph, DAG) на основе зависимостей между преобразованиями.

**Hành động** là một thao tác Spark trả về một thứ gì đó cho hệ thống bên ngoài Spark (cho người thực thi Spark). Một ví dụ sẽ là trả lại dữ liệu cho trình điều khiển (với các thao tác như đếm hoặc thu thập) hoặc ghi dữ liệu vào hệ thống lưu trữ bên ngoài. Các hành động sẽ kích hoạt bộ lập lịch, bộ lập lịch này sẽ xây dựng biểu đồ chu kỳ có hướng (DAG) dựa trên sự phụ thuộc giữa các phép biến đổi.

## Преимущества отложенных вычислений

1) Отложенные вычисления позволяют Spark объединять операции, не требующие взаимодействия с драйвером, чтобы избежать многократных проходов по данным.
2) Spark отличается отказоустойчивостью. Это значит, что он не подведет, не потеряет данные и не вернет неправильные результаты даже в случае отказа машины, на которой он работает, или сбоя сети. Уникальность обеспечения отказоустойчивости Spark состоит в следующем: каждая секция данных содержит информацию о зависимостях, достаточную для повторного ее вычисления. Следовательно, при потере секции в RDD есть достаточно информации относительно ее происхождения, чтобы вычислить ее заново, причем этот расчет можно распараллелить для ускорения восстановления.

---

1) Đánh giá lười biếng cho phép Spark kết hợp các hoạt động không yêu cầu tương tác với trình điều khiển để tránh truyền dữ liệu nhiều lần.
2) Spark có khả năng chịu lỗi. Điều này có nghĩa là nó sẽ không bị lỗi, mất dữ liệu hoặc trả về kết quả không chính xác ngay cả khi máy đang chạy bị lỗi hoặc mạng bị lỗi. Điều làm cho khả năng chịu lỗi của Spark trở nên độc đáo là mỗi phân vùng dữ liệu chứa đủ thông tin phụ thuộc để tính toán lại nó. Do đó, nếu một phần bị mất, RDD có đủ thông tin về nguồn gốc của nó để tính toán lại nó và phép tính này có thể được thực hiện song song để tăng tốc độ phục hồi.

## Хранение данных в памяти

- **В оперативной памяти в виде десериализованных Java-объектов**. Наиболее очевидный способ хранения объектов в наборе RDD — в виде исходных десериализованных Java-объектов, определяемых драйверной программной. Это самая быстродействующая форма хранения данных в оперативной памяти, поскольку экономит требуемое на сериализацию время.
- **Trong RAM ở dạng các đối tượng Java được giải tuần tự hóa**. Cách rõ ràng nhất để lưu trữ các đối tượng trong RDD là lưu trữ các đối tượng Java được giải tuần tự hóa ban đầu được xác định bởi phần mềm trình điều khiển. Đây là hình thức lưu trữ dữ liệu trong bộ nhớ nhanh nhất vì nó tiết kiệm thời gian cần thiết cho việc tuần tự hóa.
- **В виде сериализованных данных**. При перемещении по сети объекты Spark преобразуются в потоки байтов с помощью стандартной библиотеки сериализации языка Java. Это, вероятно, более медленно работающий подход, поскольку чтение сериализованных данных требует от CPU большего объема действий, чем чтение десериализованных. Однако это зачастую выгоднее в смысле используемой памяти, поскольку пользователь получает возможность выбирать наиболее эффективное представление.
- **Là dữ liệu được tuần tự hóa**. Khi các đối tượng Spark di chuyển trên mạng, chúng được chuyển đổi thành luồng byte bằng thư viện tuần tự hóa ngôn ngữ Java tiêu chuẩn. Đây có thể là một cách tiếp cận chậm hơn vì việc đọc dữ liệu được tuần tự hóa đòi hỏi nhiều công việc của CPU hơn là đọc dữ liệu đã được giải tuần tự. Tuy nhiên, điều này thường có lợi hơn về mặt sử dụng bộ nhớ, vì người dùng có thể chọn cách trình bày hiệu quả nhất.
- **На диске**. Наборы RDD, секции которых слишком велики для хранения в оперативной памяти каждого из исполнителей, можно записать на диск. Это явно более медленный метод в случае повторяемых вычислений, но, вероятно, и более отказоустойчивый при длинных последовательностях преобразований и, наверное, единственный разумный вариант при очень больших объемах вычислений.
- **Trên đĩa**. Các bộ RDD có phần quá lớn để có thể lưu trữ trong RAM của mỗi bộ thực thi có thể được ghi vào đĩa. Đây rõ ràng là một phương pháp chậm hơn trong trường hợp tính toán lặp đi lặp lại, nhưng có lẽ có khả năng chịu lỗi cao hơn đối với các chuỗi biến đổi dài và có lẽ là lựa chọn hợp lý duy nhất cho khối lượng tính toán rất lớn.

## Структура задания

```{figure} structural-task.png
```

## Пример структуры задания

```{figure} structural-task-example.png
```
