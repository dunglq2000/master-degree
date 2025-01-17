# Лекция 4. Apache Spark: Часть 2

## Структура задания

Приложение Spark соответствует набору заданий Spark, определяемому одним объектом SparkSession в драйверной программе.

Ứng dụng Spark tương ứng với một tập hợp các công việc Spark được xác định bởi một đối tượng SparkSession duy nhất trong chương trình trình điều khiển.

---

Приложение Spark «ничего не делает» до тех пор, пока драйверная программа не вызовет действие. При каждом вызове действия планировщик Spark строит граф выполнения и запускает **задание Spark** (Spark job)

Ứng dụng Spark "không làm gì" cho đến khi chương trình trình điều khiển gọi hành động. Mỗi khi một hành động được gọi, bộ lập lịch Spark sẽ xây dựng một biểu đồ thực thi và chạy **Spark job** (Spark job)

---

Задание Spark состоит из **этапов** (stage), представляющих собой шаги преобразования данных, необходимые для формирования итогового набора RDD.

Công việc Spark bao gồm **giai đoạn** (giai đoạn), là các bước chuyển đổi dữ liệu cần thiết để tạo bộ RDD cuối cùng.

---

Этап состоит из набора **задач** (tasks), каждая из которых означает параллельное вычисление, выполняемое на исполнителе. Секции в итоговом RDD данного этапа соответствует одна **задача** (task).

Một giai đoạn bao gồm một tập hợp các **tác vụ**, mỗi tác vụ đại diện cho một phép tính song song được thực hiện trên một trình thực thi. Phần trong RDD cuối cùng của giai đoạn này tương ứng với một **nhiệm vụ** (nhiệm vụ).

```{figure} 4-1.png
```

## Пример структуры задания

```scala
def simpleSparkProgramm(rdd : RDD[Double]): Long ={
    // Этап 1
    rdd.filter(_ < 1000.0)
        .map(x => (x, x))
    // Этап 2
        .groupByKey()
        .map{ case(value, groups) => (groups.sum, value)}
    // Этап 3
        .sortByKey()
        .count
}
```

```{figure} 4-2.png
```

## Основные свойства RDD

Для внутренних целей Spark использует для представления RDD пять основных свойств. Из них, три обязательных свойства.

- список объектов секций, составляющих набор RDD
- функция вычисления итератора секции
- список зависимостей от других наборов

Trong nội bộ, Spark sử dụng năm thuộc tính cơ bản để thể hiện RDD. Trong số này, có ba thuộc tính bắt buộc.

- danh sách các đối tượng phần tạo nên bộ RDD
- hàm tính toán phần lặp
- danh sách phụ thuộc vào các bộ khác

---

Пять свойств соответствуют следующим доступным конечному пользователю (то есть вам) пяти методам.

Năm thuộc tính tương ứng với năm phương thức sau đây có sẵn cho người dùng cuối (tức là bạn).

- `partitions()` — возвращает массив объектов секций, составляющих части распределенного набора данных. Если речь идет об RDD с объектом partitioner, то значение индекса каждой из секций будет соответствовать значению, возвращаемому функцией getPartition для каждого ключа данных, относящегося к этой секции.
- `partitions()` - trả về một mảng các đối tượng phân vùng tạo nên các phần của tập dữ liệu phân tán. Nếu chúng ta đang nói về một RDD có đối tượng phân vùng thì giá trị chỉ mục của mỗi phân vùng sẽ tương ứng với giá trị được hàm getPartition trả về cho từng khóa dữ liệu liên quan đến phân vùng đó.
- `iterator(p, parentIters)` — вычисляет элементы секции p с помощью заданных итераторов для каждой из ее родительских секций. Эта функция вызывается для вычисления каждой из секций данного RDD. Она не предназначена для непосредственного вызова пользователем, а применяется фреймворком Spark при вычислении действий.
- `iterator(p, parentIters)` - tính toán các phần tử của phần p bằng cách sử dụng các trình vòng lặp đã cho cho từng phần cha của nó. Hàm này được gọi để tính toán từng phần của RDD nhất định. Nó không nhằm mục đích được người dùng gọi trực tiếp mà được sử dụng bởi khung Spark khi tính toán các hành động.
- `dependencies()` — возвращает последовательность объектов зависимостей. Благодаря зависимостям планировщик знает, как данный RDD зависит от других. Существует два вида зависимостей: узкие (объекты NarrowDependency), соответствующие секциям, зависящим от одной или небольшого количества родительских секций, и широкие (объекты ShuffleDependency), используемые в случаях, когда для вычисления секции необходима перегруппировка всех данных из родительских секций. Мы обсудим эти типы зависимостей в подразделе «Широкие и узкие зависимости» далее в текущем разделе.
- `dependency()` - trả về một chuỗi các đối tượng phụ thuộc. Nhờ sự phụ thuộc, bộ lập lịch biết RDD nhất định phụ thuộc vào người khác như thế nào. Có hai loại phụ thuộc: hẹp (đối tượng Phụ thuộc hẹp), tương ứng với các phân vùng phụ thuộc vào một hoặc một số ít phân vùng cha và rộng (đối tượng ShuffleDependency), được sử dụng trong trường hợp cần tập hợp lại tất cả dữ liệu từ phân vùng cha để tính toán phân vùng. Chúng ta sẽ thảo luận về các loại phụ thuộc này trong tiểu mục “Phụ thuộc rộng và hẹp” ở phần sau của phần này.
- `partitioner()` — возвращает вариантный тип Scala для объекта partitioner, если между element и partition объекта RDD есть связанная с ним функция, например hashPartitioner. Эта функция возвращает None для всех наборов RDD, чей тип не кортеж (которые не представляют данные типа «ключ — значение»). У представляющего HDFS-файл набора (реализован в NewHadoopRDD.scala) каждому блоку файла соответствует секция.
- `partitioner()` - Trả về loại biến thể Scala cho một đối tượng phân vùng nếu có hàm liên kết giữa phần tử và phân vùng của đối tượng RDD, chẳng hạn như hashPartitioner. Hàm này trả về Không có cho tất cả các RDD có loại không phải là bộ dữ liệu (không biểu thị dữ liệu khóa-giá trị). Tập hợp đại diện cho tệp HDFS (được triển khai trong NewHadoopRDD.scala) có phần tương ứng cho mỗi khối của tệp.
- `preferredLocations(p)` — возвращает информацию о локальности данных секции p. Точнее говоря, эта функция возвращает последовательность строк с информацией о каждом из узлов, на которых хранятся фрагменты p. В случае представляющего HDFS-файл набора RDD каждая строка возвращаемого функцией preferredLocations результата представляет собой Hadoop-имя узла, в котором хранится данная секция.
- `preferredLocations(p)` - trả về thông tin về vị trí dữ liệu của phần p. Chính xác hơn, hàm này trả về một chuỗi các chuỗi có thông tin về từng nút lưu trữ các đoạn của p. Trong trường hợp một tập hợp RDD đại diện cho tệp HDFS, mỗi hàng kết quả được trả về bởi hàm PreferLocations đại diện cho tên Hadoop của nút trong đó phần này được lưu trữ.

## Широкие и узкие зависимости

Самая важная информация, которую нужно знать о преобразованиях для понимания механизма вычисления наборов RDD, — то, что они делятся на две категории:

- преобразования с узкими зависимостями (narrow dependencies)
- преобразования с широкими зависимостями (wide dependencies).

Thông tin quan trọng nhất bạn cần biết về các phép biến đổi để hiểu cách tính các bộ RDD là chúng thuộc hai loại:

- biến đổi với sự phụ thuộc hẹp
- biến đổi với sự phụ thuộc rộng rãi.

```{figure} 4-3.png
```

## Форматы файлов Big Data

Все многообразие файловых форматов Big Data (AVRO, Sequence, Parquet, ORC, RCFile) можно разделить на 2 категории: **линейные** (строковые) и **колоночные** (столбцовые).

Toàn bộ các định dạng tệp Dữ liệu lớn (AVRO, Sequence, Parquet, ORC, RCFile) có thể được chia thành 2 loại: **tuyến tính** (hàng) và **cột** (cột).

- **В линейных форматах** (AVRO, Sequence) строки данных одного типа хранятся вместе, образуя непрерывное хранилище. Даже если необходимо получить лишь некоторые значения из строки, все равно вся строка будет считана с диска в память.
- **Ở định dạng tuyến tính** (AVRO, Sequence), các hàng dữ liệu cùng loại được lưu trữ cùng nhau, tạo thành một kho lưu trữ liền kề. Ngay cả khi bạn chỉ cần lấy một số giá trị từ một chuỗi thì toàn bộ chuỗi đó vẫn sẽ được đọc từ đĩa vào bộ nhớ.
- Линейный способ хранения данных обусловливает пониженную скорость операций чтения и выполнении избирательных запросов, а также больший расход дискового пространства.
- Phương pháp lưu trữ dữ liệu tuyến tính khiến tốc độ đọc và thực hiện các truy vấn chọn lọc thấp hơn cũng như tiêu tốn nhiều dung lượng ổ đĩa hơn.
- Степень сжатия информации у строковых форматов ниже, чем у столбцовых.
- Mức độ nén thông tin đối với định dạng hàng thấp hơn so với định dạng cột.
- Линейно-ориентированные форматы лучше всего подходят для потоковой записи, т.к. в случае сбоя информация может быть восстановлена (повторно синхронизирована) с последней точки синхронизации.
- Các định dạng hướng dòng phù hợp nhất để ghi trực tuyến vì... Trong trường hợp xảy ra lỗi, thông tin có thể được khôi phục (đồng bộ lại) từ điểm đồng bộ hóa cuối cùng.

```{figure} 4-4.png
```

**В колоночно-ориентированных форматах** (Parquet, RCFile, ORCFile) файл разрезается на несколько столбцов данных, которые хранятся вместе, но могут быть обработаны независимо друг от друга.

**Ở các định dạng hướng theo cột** (Parquet, RCFile, ORCFile), tệp được cắt thành nhiều cột dữ liệu được lưu trữ cùng nhau nhưng có thể được xử lý độc lập với nhau.

- Метод хранения информации позволяет пропускать ненужные столбцы при чтении данных, что существенно ускоряет чтение данных и отлично подходит в случае, когда необходим небольшой объем строк или выполняются избирательные запросы
- Phương pháp lưu trữ thông tin cho phép bạn bỏ qua các cột không cần thiết khi đọc dữ liệu, giúp tăng tốc đáng kể việc đọc dữ liệu và rất tuyệt vời khi cần một lượng hàng nhỏ hoặc thực hiện các truy vấn chọn lọc
- Такой формат чтения и записи занимает больше места в оперативной памяти, поскольку, чтобы получить столбец из нескольких строк, кэшируется каждая строка.
- Định dạng đọc-ghi này chiếm nhiều dung lượng RAM hơn vì mỗi hàng được lưu vào bộ đệm để lấy một cột gồm nhiều hàng.
- Колоночно-ориентированные форматы не используются в средах потоковой обработки (Apache Kafka, Flume), т.к. после сбоя записи текущий файл не сможет быть восстановлен из-за отсутствия точек синхронизации.
- Các định dạng hướng theo cột không được sử dụng trong môi trường xử lý luồng (Apache Kafka, Flume), vì Sau khi ghi thất bại, tệp hiện tại không thể được khôi phục do thiếu điểm đồng bộ hóa.
- Колоночные файлы занимают меньше места на жестком диске вследствие более эффективного сжатия информации по столбцам
- Tệp cột chiếm ít dung lượng trên ổ cứng của bạn hơn do nén thông tin qua các cột hiệu quả hơn

```{figure} 4-5.png
```

## Форматы файлов Big Data/Parquet

**Apache Parquet** — это бинарный, колоночно-ориентированный (столбцовый) формат хранения больших данных.

**Apache Parquet** là định dạng nhị phân, định hướng theo cột để lưu trữ dữ liệu lớn.

---

Созданный специально для экосистемы Hadoop, он позволяет эффективно сжимать информацию и считывать файлы частично, по мере необходимых столбцов. **Паркет** предоставляет возможность задавать схемы сжатия на уровне столбцов и добавлять новые кодировки по мере их изобретения и реализации.

Được thiết kế dành riêng cho hệ sinh thái Hadoop, nó cho phép bạn nén thông tin một cách hiệu quả và đọc một phần tệp theo các cột bắt buộc. **Sàn gỗ** cung cấp khả năng chỉ định các sơ đồ nén cấp cột và thêm các mã hóa mới khi chúng được phát minh và triển khai.

---

Паркет поддерживает наиболее распространенные типы данных (boolean, int32, int64, int96, float, double, byte_array) и реализует многоуровневую систему разбиения файлов на части (группы строк, блок данных столбца и разбиение столбцов по страницам), благодаря чему обеспечивается высокая скорость работы с данными.

---

Parquet hỗ trợ các loại dữ liệu phổ biến nhất (boolean, int32, int64, int96, float, double, byte_array) và triển khai hệ thống đa cấp để chia tệp thành các phần (nhóm hàng, khối dữ liệu cột và phân trang cột), đảm bảo tốc độ cao về làm việc với dữ liệu.

---

### Плюсы

- **экономия места** для хранения данных за счет эффективного сжатия информации по столбцам– в частности, по сравнению с Apache Avro, другим популярным форматом Big Data, Паркет сжимает данные примерно в 3,5 раза лучше;
- **tiết kiệm không gian** để lưu trữ dữ liệu nhờ nén thông tin hiệu quả giữa các cột – đặc biệt, so với Apache Avro, một định dạng Dữ liệu lớn phổ biến khác, Parquet nén dữ liệu tốt hơn khoảng 3,5 lần;
- **высокая скорость** чтения данных и отработки запросов, извлекающих определенные значения столбцов вместо считывания всего большого файла, что значительно ускоряет работу аналитика Big Data;
- **tốc độ cao** đọc dữ liệu và chạy truy vấn truy xuất các giá trị cột cụ thể thay vì đọc toàn bộ tệp lớn, giúp tăng tốc đáng kể công việc của nhà phân tích Dữ liệu lớn;
- **возможность реализации собственных схем данных** и применения различных методов кодирования к различным столбцам;
- **khả năng triển khai sơ đồ dữ liệu của riêng bạn** và áp dụng các phương pháp mã hóa khác nhau cho các cột khác nhau;
- **поддержка нескольких языков программирования** (C++, Java, Python, PHP и т.д.), а также популярных реймворков, например, Apache Thrift, что повышает гибкость формата;
- **hỗ trợ một số ngôn ngữ lập trình** (C++, Java, Python, PHP, v.v.), cũng như các khung phổ biến, ví dụ: Apache Thrift, giúp tăng tính linh hoạt của định dạng;
- **возможность хранения данных не только в HDFS**, для которой Parquet и был создан изначально, но и в других файловых системах (GlusterFs, NFS и пр.);
- **khả năng lưu trữ dữ liệu không chỉ trong HDFS**, Parquet được tạo ban đầu mà còn trong các hệ thống tệp khác (GlusterFs, NFS, v.v.);
- **простота и удобство работы с файлами** с помощью операций перемещения, резервного копирования и реплицирования;
- **đơn giản và thuận tiện khi làm việc với các tập tin** bằng cách sử dụng các thao tác di chuyển, sao lưu và sao chép;
- **поддержка Apache Spark «по умолчанию»** (из коробки) обеспечивает возможность сохранить файл Big Data в другое облачное или локальное хранилище данных.
- **Hỗ trợ Apache Spark “theo mặc định”** (có sẵn) cung cấp khả năng lưu tệp Dữ liệu lớn vào một đám mây khác hoặc bộ lưu trữ dữ liệu cục bộ.

### Минусы

- **строгая типизация данных** – в связи с колоночной ориентацией файл формата Паркет ведёт себя как неизменяемая таблица или база данных, когда для столбца четко определён тип данных, при этом невозможно его изменить или скомбинировать, например, объединив вложенный json с простым строковым значением.
- **gõ dữ liệu nghiêm ngặt** – do hướng cột, tệp định dạng Parquet hoạt động giống như một bảng hoặc cơ sở dữ liệu bất biến khi loại dữ liệu cho một cột được xác định rõ ràng và không thể thay đổi hoặc kết hợp nó, chẳng hạn như: bằng cách kết hợp json lồng nhau với ý nghĩa chuỗi đơn giản.
- **отсутствие встроенной (нативной) поддержки** в других фреймворках Big Data, кромеApache Spark;
- **thiếu hỗ trợ tích hợp (gốc)** trong các khung Dữ liệu lớn khác ngoại trừ Apache Spark;
- **отсутствие возможности отслеживать изменение данных** и эволюцию схемы, в отличие от, например, Avro, другого популярного форматом Big Data, изменение схемы данных которого легко прослеживается через графический интерфейс Sсhema Registry в Apache Kafka Confluent (об этом мы писали здесь). Отметим, что Apache Spark позволяет объединять схемы данных при изменении их со временем, но для этого требуется указать специальную опцию при чтении. А, чтобы что-то изменить в уже существующим файле, его придется перезаписать или добавить новую колонку.
- **thiếu khả năng theo dõi các thay đổi dữ liệu** và tiến hóa lược đồ, chẳng hạn như Avro, một định dạng Dữ liệu lớn phổ biến khác, những thay đổi trong lược đồ dữ liệu có thể dễ dàng theo dõi thông qua giao diện đồ họa Schema Register trong Apache Kafka Confluent (chúng tôi đã viết về điều này ở đây). Lưu ý rằng Apache Spark cho phép bạn hợp nhất các lược đồ dữ liệu khi chúng thay đổi theo thời gian, nhưng điều này yêu cầu bạn chỉ định một tùy chọn đặc biệt khi đọc. Và để thay đổi nội dung nào đó trong tệp hiện có, bạn sẽ phải ghi đè lên tệp đó hoặc thêm cột mới.
- **не поддерживаются транзакции**, поскольку, несмотря на некоторую схожесть с базой данных (в части строгой типизации), файлы формата Паркет– это частично размеченная информация.
- **giao dịch không được hỗ trợ**, bởi vì, mặc dù có một số điểm tương đồng với cơ sở dữ liệu (về mặt gõ nghiêm ngặt), các tệp định dạng Parquet vẫn được đánh dấu một phần thông tin.
- **сложность частичной потоковой передачи данных** - необходимо передавать всю «группу строк»;
- **sự phức tạp của việc truyền dữ liệu một phần** - cần phải truyền toàn bộ “nhóm hàng”;
- **сильная привязка к метаданным** – при повреждении, потере метаданных или изменении контрольной суммы группы строк, блока данных столбца или страницы данных, вся смысловая информация будет утеряна. Отметим, что, отключив в файловой системе вычисления контрольных сумм на каждом из уровней разбиения, можно значительно повысить производительность;
- **ràng buộc chặt chẽ với siêu dữ liệu** – nếu siêu dữ liệu bị hỏng, bị mất hoặc tổng kiểm tra của một nhóm hàng, khối dữ liệu cột hoặc trang dữ liệu bị thay đổi thì tất cả thông tin ngữ nghĩa sẽ bị mất. Lưu ý rằng bằng cách vô hiệu hóa tính toán tổng kiểm tra ở mỗi cấp độ phân vùng trong hệ thống tệp, hiệu suất có thể được cải thiện đáng kể;
- **Паркетнеявляется человекочитаемым форматом**, в отличие, например, от JSON или CSV.
- **Sàn gỗ không phải là định dạng mà con người có thể đọc được**, không giống như JSON hoặc CSV chẳng hạn.

## Наборы DataFrame и Spark SQL

Интерфейсы **DataFrame** и **Dataset Модуля Spark SQL** обеспечивают более эффективные варианты хранения данных, продвинутый оптимизатор и операции непосредственно над сериализованными данными.

**Giao diện **DataFrame** và **Bộ dữ liệu của Mô-đun Spark SQL** cung cấp các tùy chọn lưu trữ dữ liệu hiệu quả hơn, trình tối ưu hóa nâng cao và các thao tác trực tiếp trên dữ liệu được tuần tự hóa.

---

Наборы DataFrame и Dataset представляют собой распределенные коллекции с отсутствующей в RDD дополнительной информацией о схеме.

DataFrames và Datasets là các bộ sưu tập được phân phối với thông tin lược đồ bổ sung bị thiếu trong RDD.

```{figure} 4-6.png
```

- Набор DataFrame представляет собой набор Dataset специальных объектов типа Row у которого отсутствует какая либо проверка типа на этапе компиляции.
- Tập DataFrame là tập hợp các Dataset gồm các đối tượng đặc biệt thuộc kiểu Row và không được kiểm tra kiểu ở giai đoạn biên dịch.
- Наборы DataFrame представляют собой распределенные коллекции с отсутствующей в RDD дополнительной информацией о схеме.
- DataFrames là các bộ sưu tập được phân phối với thông tin lược đồ bổ sung bị thiếu trong RDD.
- Посравнению с применением наборов RDD при обращении к DataFrame оптимизатор Spark может лучше понять наш код и наши данные, благодаря чему становится оптимизация лучше.
- So với việc sử dụng bộ RDD khi truy cập DataFrame, trình tối ưu hóa Spark có thể hiểu mã và dữ liệu của chúng tôi tốt hơn, dẫn đến tối ưu hóa tốt hơn.
- Наборы DataFrame модуля Spark SQL позволяет работать с наборами DataFrame, не прибегая к регистрации временных таблиц или генерации SQL-выражений.
- Bộ khung dữ liệu Mô-đun Spark SQL cho phép bạn làm việc với các bộ DataFrame mà không cần phải đăng ký các bảng tạm thời hoặc tạo biểu thức SQL.
- НаборыDataFrame включает как преобразования, так и действия.
- Bộ DataFrame bao gồm cả chuyển đổi và hành động.

```{figure} 4-7.png
```

- Объект SparkSession обычно создается с помощью паттерна «Строитель» (Builder) и метода `getOrCreate()`, возвращающего текущий сеанс, если таковой уже существует.
- Đối tượng SparkSession thường được tạo bằng cách sử dụng mẫu Builder và phương thức `getOrCreate()` để trả về phiên hiện tại nếu đã tồn tại.
- «Строитель» принимает на входе ключи конфигурации в строковом виде `config(key, value)` и сокращения, имеющиеся для множества распространенных параметров.
- "Builder" nhận làm khóa cấu hình đầu vào ở dạng chuỗi `config(key, value)` và các chữ viết tắt có sẵn cho nhiều tham số phổ biến.
- enableHiveSupport(), обеспечивающее доступ к пользовательским функциям UDF СУБД Hive без необходимости установить Hive
- EnableHiveSupport(), cung cấp quyền truy cập vào các chức năng người dùng Hive DBMS UDF mà không cần cài đặt Hive

```{figure} 4-8.png
```

- Объект SparkContext Можно использовать его для создания RDD из локального объекта Scala (с применением одного из методов makeRDD или parallelize) или с помощью чтения данных из устойчивого.
- Đối tượng SparkContext Bạn có thể sử dụng nó để tạo RDD từ một đối tượng Scala cục bộ (sử dụng một trong các phương thức makeRDD hoặc song song) hoặc bằng cách đọc dữ liệu từ Persist.
- Объекты DataFrame и Dataset можно читать, задействуя SparkSession — объект Spark SQL, эквивалентный SparkContext.
- Các đối tượng DataFrame và Dataset có thể được đọc bằng SparkSession, một đối tượng Spark SQL tương đương với SparkContext.
- ВSpark метод `createDataFrame()` используется для создания DataFrame вручную. Используя этот метод, вы можете создать Spark DataFrame из уже существующих объектов данных RDD.
- Trong Spark, phương thức `createDataFrame()` được sử dụng để tạo DataFrame theo cách thủ công. Sử dụng phương pháp này, bạn có thể tạo Spark DataFrame từ các đối tượng dữ liệu RDD hiện có.

```{figure} 4-9.png
```
