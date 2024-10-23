# Лекция 1

## OLTP-системы

**Основное назначение OLTP-систем** – это быстрая обработка небольших операций изменения данных (добавление, редактирование, удаление), поступающих большим потоком в режиме реального времени.

**Mục đích chính của hệ thống OLTP** là xử lý nhanh các hoạt động sửa đổi dữ liệu nhỏ (thêm, chỉnh sửa, xóa) nhận được trong các luồng lớn trong thời gian thực.

**Основное требование к таким системам** – это обеспечение выполнения операций в рамках заданных временных ограничений.

**Yêu cầu chính đối với các hệ thống như vậy** là đảm bảo rằng các hoạt động được hoàn thành trong giới hạn thời gian quy định.

Область применения таких систем крайне широка. Это может быть информационная система магазина, в которой, прежде всего, необходимо быстро оформить и сохранить записи о совершённых покупках. Это может быть информационная система оперативной обработки банковских транзакций.

Phạm vi ứng dụng của các hệ thống như vậy là vô cùng rộng. Đây có thể là một hệ thống thông tin cửa hàng, trong đó trước hết cần phải nhanh chóng tạo và lưu lại hồ sơ các giao dịch mua đã thực hiện. Đây có thể là một hệ thống thông tin phục vụ hoạt động xử lý các giao dịch ngân hàng.

Это может быть и часть полноценной ERP-системы (Enterprise Resource Planning, планирование ресурсов предприятия) крупной промышленной организации, отвечающая за ввод операционной информации.

Nó cũng có thể là một phần của hệ thống ERP (Kế hoạch nguồn lực doanh nghiệp) chính thức của một tổ chức công nghiệp lớn, chịu trách nhiệm nhập thông tin hoạt động.

Так как во главу угла в OLTP-системах ставится скорость обработки небольших транзакций, то в них база данных обычно проектируется в сильно нормализованном виде.

Vì tốc độ xử lý các giao dịch nhỏ là hết sức quan trọng trong các hệ thống OLTP nên cơ sở dữ liệu trong chúng thường được thiết kế ở dạng chuẩn hóa cao.

То есть, если говорить совсем упрощённо, большие таблицы разделяются на минимальные смысловые порции, образующие много маленьких (по количеству полей) таблиц.

Nghĩa là, nói một cách rất đơn giản, các bảng lớn được chia thành các phần ngữ nghĩa tối thiểu, tạo thành nhiều bảng nhỏ (về số lượng trường).

Очень часто OLTP-системы содержат информацию актуальную только в текущий момент или в течении небольшого периода. Для долговременных исследований, требующих данные за длительные периоды времени OLTP-системы не подходят.

Rất thường xuyên, hệ thống OLTP chứa thông tin chỉ có liên quan tại thời điểm hiện tại hoặc trong một khoảng thời gian ngắn. Đối với các nghiên cứu dài hạn đòi hỏi dữ liệu trong thời gian dài, hệ thống OLTP không phù hợp.

Обычно каждая OLTP-система отвечают за свою довольно узкую часть бизнес процесса кампании и содержит минимально требуемую детализацию данных.

Thông thường, mỗi hệ thống OLTP chịu trách nhiệm về một phần khá hẹp của quy trình kinh doanh chiến dịch và chứa chi tiết dữ liệu bắt buộc tối thiểu.

Таким образом, использовать OLTP-системы в чистом виде для серьезных аналитических или предиктивных исследований затруднительно.

Vì vậy, rất khó để sử dụng các hệ thống OLTP ở dạng thuần túy cho nghiên cứu phân tích hoặc dự đoán nghiêm túc.

## DSS-системы

В противоположность OLTP-системам, основной целью систем поддержки принятия решений является не быстрое преоброзование данных, а предоставление аналитических и предиктивных механизмов.

Ngược lại với các hệ thống OLTP, mục tiêu chính của hệ thống hỗ trợ quyết định không phải là chuyển đổi dữ liệu nhanh chóng mà là cung cấp các cơ chế phân tích và dự đoán.

Обычно DSS-системы аккумулируют данные из нескольких источников и/или за длительный период времени.

Thông thường, hệ thống DSS tích lũy dữ liệu từ nhiều nguồn và/hoặc trong một khoảng thời gian dài.

В зависимости от назначения DSS-системы могут решать разные задачи. Это могут быть простые системы, которые при помощи заранее написанных запросов формируют различные статистические данные. Например, сводную информацию о продажах за месяц по всем точкам дистрибьюторской сети. Это могут быть системы, позволяющие формировать произвольные статистические запросы с различными элементами агрегаций данных. И это могут быть системы, позволяющие выявить на основе имеющихся данных новые. Например, выполнить прогнозирование расходов топлива в ближайшие месяцы на основе собранных за последние пять лет данных.

Tùy thuộc vào mục đích của chúng, hệ thống DSS có thể giải quyết các vấn đề khác nhau. Đây có thể là những hệ thống đơn giản tạo ra nhiều dữ liệu thống kê khác nhau bằng cách sử dụng các truy vấn được viết sẵn. Ví dụ: thông tin tóm tắt về doanh số bán hàng trong tháng cho tất cả các điểm của mạng lưới phân phối. Đây có thể là các hệ thống cho phép bạn tạo các truy vấn thống kê tùy ý với nhiều yếu tố tổng hợp dữ liệu khác nhau. Và đây có thể là những hệ thống cho phép chúng tôi xác định những hệ thống mới dựa trên dữ liệu hiện có. Ví dụ: dự báo mức tiêu thụ nhiên liệu trong những tháng tới dựa trên dữ liệu được thu thập trong 5 năm qua.

Данные **в DSS-системы поступают редко** (по сравнению с OLTP- системами). Причём обычно это происходит автоматическим путём, а не при помощи оператора. Работают с DSS-системами аналитики. Как следствие, минимальное время отклика уже не так важно. Аналитик может ждать результата и несколько часов.

Dữ liệu **hiếm khi vào hệ thống DSS** (so với hệ thống OLTP). Hơn nữa, điều này thường xảy ra tự động và không có sự trợ giúp của người vận hành. Làm việc với các hệ thống phân tích DSS. Kết quả là thời gian phản hồi tối thiểu không còn quá quan trọng nữa. Nhà phân tích có thể đợi vài giờ để có kết quả.

Так как работа идёт не одной записью, а с большим числом подробно разобранных данных, то для **DSS-систем характерно применение** денормализации данных.

Vì công việc không được thực hiện với một bản ghi mà với một số lượng lớn dữ liệu chi tiết, **hệ thống DSS thường sử dụng** không chuẩn hóa dữ liệu.

## Data Mining

Особым видов DSS-систем являются системы, помогающие аналитику обнаружить новые, заранее ему неизвестные знания в имеющемся в его распоряжении наборе данных.

Một loại hệ thống DSS đặc biệt là hệ thống giúp nhà phân tích khám phá những kiến ​​thức mới, chưa biết trước đây trong tập dữ liệu mà họ có thể tùy ý sử dụng.

Такой процесс называется **интеллектуальным анализом данных**.

Quá trình này được gọi là **khai thác dữ liệu**.

В англоязычной литературе он более известен под термином Data Mining.

Trong tài liệu tiếng Anh, nó được biết đến nhiều hơn với thuật ngữ Khai thác dữ liệu.

## Основные этапы

Любая DSS-система обычно решает следующие задачи:

1) сбор информации;
2) преобразование информации;
3) хранение информации;
4) представление информации в виде, пригодном для аналитического исследования и (но не обязательно) выявление новых знаний методами Data Mining.

Bất kỳ hệ thống DSS nào cũng thường giải quyết được các vấn đề sau:

1) thu thập thông tin;
2) chuyển đổi thông tin;
3) lưu trữ thông tin;
4) trình bày thông tin dưới dạng phù hợp cho nghiên cứu phân tích và (nhưng không nhất thiết) xác định kiến ​​thức mới bằng các phương pháp Khai thác dữ liệu.

Очевидно, что решать задачи Data Mining не возможно без решения первых трёх задач.

Rõ ràng là không thể giải quyết các vấn đề Khai thác dữ liệu nếu không giải quyết được ba vấn đề đầu tiên.

## Озеро Данных – Data Lake

Data lake — это огромное хранилище, которое принимает любые файлы всех форматов. Источник данных тоже не имеет никакого значения. Озеро данных может принимать данные из CRM- или ERP- систем, продуктовых каталогов, банковских программ, датчиков или умных устройств — любых систем, которые использует бизнес.

Hồ dữ liệu là một kho lưu trữ khổng lồ chấp nhận mọi tệp ở mọi định dạng. Nguồn dữ liệu cũng không thành vấn đề. Hồ dữ liệu có thể nhận dữ liệu từ hệ thống CRM hoặc ERP, danh mục sản phẩm, chương trình ngân hàng, cảm biến hoặc thiết bị thông minh - bất kỳ hệ thống nào mà doanh nghiệp sử dụng.

## Некоторые термины и понятия

**ETL** – аббревиатура от Extract, Transform, Load. один из основных процессов в управлении хранилищами данных, который включает в себя:

1. извлечение данных из внешних источников;
2. их трансформация и очистка, чтобы они соответствовали
3. потребностям бизнес-модели;
4. и загрузка их в хранилище данных.

**ETL** là từ viết tắt của Extract, Transform, Load. một trong những quy trình chính trong quản lý kho dữ liệu, bao gồm:

1. trích xuất dữ liệu từ các nguồn bên ngoài;
2. biến đổi chúng và làm sạch chúng sao cho phù hợp
3. nhu cầu về mô hình kinh doanh;
4. và tải chúng vào kho dữ liệu.

**ELT** – это другой метод рассмотрения инструментального подхода к перемещению данных. Вместо преобразования данных перед их записью ELT позволяет целевой системе выполнить преобразование. Данные сначала копируются в цель, а затем преобразуются на место.

**ELT** là một cách khác để xem xét cách tiếp cận thiết bị đo đạc đối với việc di chuyển dữ liệu. Thay vì chuyển đổi dữ liệu trước khi ghi, ELT cho phép hệ thống đích thực hiện chuyển đổi. Dữ liệu đầu tiên được sao chép vào mục tiêu và sau đó được chuyển thành vị trí.

## Обоснование актуальности применения распределенных технологий

**Большие данные** – это наборы данных такого объёма, что традиционные инструменты
не способны осуществлять их захват, управление и обработку за приемлемое для практики время.

**Dữ liệu lớn** là các tập dữ liệu có kích thước mà các công cụ truyền thống
không thể nắm bắt, kiểm soát và xử lý chúng trong thời gian thực hành có thể chấp nhận được.


> Большие данные объединяют техники и технологии, которые извлекают смысл из данных на экстремальном пределе практичности

> Dữ liệu lớn tập hợp các kỹ thuật và công nghệ trích xuất ý nghĩa từ dữ liệu ở mức cực kỳ thực tế

### Парадигма больших данных

**3 группы задач:**

* хранение и управление объёмом данных в сотни терабайт или петабайт, которые обычные реляционные базы данных не позволяют эффективно использовать
* организация неструктурированной информации, состоящей из текстов, изображений, видео и других типов данных
* анализ Big Data, рассматривающий способы работы с неструктурированной информацией, генерацию аналитических отчётов и внедрение прогностических моделей.

**3 nhóm nhiệm vụ:**

* lưu trữ và quản lý khối lượng dữ liệu hàng trăm terabyte hoặc petabyte, cơ sở dữ liệu quan hệ thông thường không cho phép sử dụng hiệu quả
* tổ chức thông tin phi cấu trúc bao gồm văn bản, hình ảnh, video và các loại dữ liệu khác
* phân tích Dữ liệu lớn, xem xét các cách làm việc với thông tin phi cấu trúc, tạo báo cáo phân tích và triển khai các mô hình dự đoán.

**Направления работы экспертов по большим данным:**

1. Аналитикой занимаются Data Scientist и Data Analyst, в их обязанности входит формирование гипотез, поиск закономерностей в наборах данных (dataset), визуализация информации, подготовка данных к моделированию, разработка алгоритмов Machine Learning (машинного обучения), интерпретация полученных данных, а также изучение предметной области или бизнес-процесса.
2. Инженерия относится к профессиям Data Engineer и администратор. Такие специалисты занимаются поддержкой, созданием и настройкой программной и аппаратной инфраструктуры системы сбора, хранения и обработки информации, а также аналитикой массивов и информационных потоков, в том числе конфигурированием облачных (Cloud) и локальных кластеров.

**Lĩnh vực làm việc của chuyên gia dữ liệu lớn:**

1. Nhà khoa học dữ liệu và Nhà phân tích dữ liệu tham gia phân tích; trách nhiệm của họ bao gồm hình thành các giả thuyết, tìm kiếm các mẫu trong tập dữ liệu, trực quan hóa thông tin, chuẩn bị dữ liệu để lập mô hình, phát triển thuật toán Machine Learning, diễn giải dữ liệu thu được và nghiên cứu lĩnh vực chủ đề hoặc quy trình kinh doanh .
2. Kỹ thuật là ngành nghề Kỹ sư dữ liệu và Quản trị viên. Các chuyên gia như vậy tham gia vào việc hỗ trợ, tạo và định cấu hình cơ sở hạ tầng phần mềm và phần cứng của hệ thống để thu thập, lưu trữ và xử lý thông tin cũng như phân tích các mảng và luồng thông tin, bao gồm định cấu hình đám mây và cluster cục bộ.

**Для работы с большими данными, необходимо иметь базовые знания:**

1. Архитектуры компьютеров и серверов;
2. Работы операционных систем и их взаимодействия с железом;
3. СУБД (MySQL, Oracle, Postgres, Amazon Redshift, Microsoft Azure, Mongo, Hadoop, BigQuery или др.);
4. По математическому анализу;
5. По теории вероятностей и статистике.

**Để làm việc với dữ liệu lớn, bạn phải có kiến ​​thức cơ bản:**

1. Kiến trúc máy tính và máy chủ;
2. Hoạt động của hệ điều hành và sự tương tác của chúng với phần cứng;
3. DBMS (MySQL, Oracle, Postgres, Amazon Redshift, Microsoft Azure, Mongo, Hadoop, BigQuery, v.v.);
4. Về phân tích toán học;
5. Về lý thuyết xác suất và thống kê.

## Введение в Hadoop

**Кластер** - несколько машин, соединенных друг с другом и взаимодействующих для выполнения общей работы.

**Cluster** - một số máy được kết nối với nhau và tương tác để thực hiện công việc chung.

**Распределённые вычисления** - способ решения трудоёмких вычислительных задач с использованием нескольких компьютеров, чаще всего объединённых в параллельную
вычислительную систему.

**Distributed computing** - một phương pháp giải các bài toán tính toán tốn nhiều công sức bằng cách sử dụng nhiều máy tính, thường được kết hợp song song
hệ thống máy tính.

**Hadoop** - это ПО с открытым исходным кодом, предназначенный для создания и запуска распределенных приложений, обрабатывающих большие объемы данных.

**Hadoop** là phần mềm nguồn mở được thiết kế để xây dựng và chạy các ứng dụng phân tán xử lý khối lượng dữ liệu lớn.

---

**Отличительные особенности Hadoop**

**Доступность** – Hadoop работает на крупных кластерах, собранных из стандартных компьютеров, или в вычислительном облаке, например на базе службы Elastic Compute Cloud (EC2 ), предлагаемой компанией Amazon.

**Надежность** – поскольку Hadoop должен работать на стандартном оборудовании, его архитектура разработана с учетом возможности частых отказов. Большинство отказов можно обработать так, что характеристики кластера будут ухудшаться постепенно.

**Масштабируемость** – Hadoop масштабируется линейно, то есть при увеличении объема данных достаточно добавить новые узлы в кластер.

**Простота** – Hadoop позволяет пользователю быстро создавать эффективный параллельный код.

**Tính năng của Hadoop**

**Tính khả dụng** – Hadoop chạy trên các cluster máy tính tiêu chuẩn lớn hoặc trong môi trường điện toán đám mây như Đám mây điện toán đàn hồi (EC2) của Amazon.

**Độ tin cậy** – Vì Hadoop phải chạy trên phần cứng thông thường nên kiến ​​trúc của nó được thiết kế để chịu được các lỗi thường xuyên. Hầu hết các lỗi có thể được xử lý để hiệu suất của cluster giảm dần.

**Khả năng mở rộng** – Hadoop chia tỷ lệ tuyến tính, nghĩa là khi khối lượng dữ liệu tăng lên, chỉ cần thêm các nút mới vào cluster là đủ.

**Đơn giản** – Hadoop cho phép người dùng nhanh chóng tạo mã song song hiệu quả.

---

1. **Кластер Hadoop** состоит из многих машин, которые хранят и параллельно обрабатывают большие наборы данных. Клиентские компьютеры посылают в это вычислительное облако задания и получают результаты.
2. **Hadoop** представляет собой набор стандартных компьютеров, объединенных в сеть, физически расположенную в одном месте.
3. Как хранение, так и обработка данных происходят внутри этого «облака» машин.

---

1. **cluster Hadoop** bao gồm nhiều máy lưu trữ và xử lý song song các tập dữ liệu lớn. Máy khách gửi công việc tới đám mây điện toán này và nhận kết quả.
2. **Hadoop** là tập hợp các máy tính tiêu chuẩn được kết nối với mạng được đặt ở một nơi.
3. Cả việc lưu trữ và xử lý dữ liệu đều diễn ra trong “đám mây” máy móc này.

## Часть 2: Введение в теорию баз данных. Язык SQL.

Некоторые тезисы:

1. СУБД на SQL ориентирован на работу со структурированными данными.
2. Hadoop имеют дело как со структурированными данными так и с неструктурированными данными, например текстовыми. С этой точки зрения, Hadoop предлагает более общую парадигму, чем SQL.
3. SQL и Hadoop могут дополнять друг друга, поскольку SQL – это язык запросов, который можно реализовать поверх Hadoop, выступающего в роли подсистемы исполнения.

Một số lưu ý:

1. SQL DBMS tập trung vào làm việc với dữ liệu có cấu trúc.
2. Hadoop xử lý cả dữ liệu có cấu trúc và dữ liệu phi cấu trúc, chẳng hạn như văn bản. Từ quan điểm này, Hadoop đưa ra một mô hình tổng quát hơn SQL.
3. SQL và Hadoop có thể bổ sung cho nhau vì SQL là ngôn ngữ truy vấn có thể được triển khai trên Hadoop, hoạt động như một công cụ thực thi.

## Сравнение СУБД с Hadoop

**Основные отличия:**

1. Масштабирование по горизонтали, а не по вертикали
2. Можно хранить данные как Пары ключ/значение вместо реляционных таблиц
3. Функциональное программирование (MapReduce) вместо декларативных запросов (SQL)
4. Автономная пакетная обработка вместо оперативных транзакций

**Sự khác biệt chính:**

1. Chia tỷ lệ theo chiều ngang, không theo chiều dọc
2. Bạn có thể lưu trữ dữ liệu dưới dạng Cặp khóa/giá trị thay vì Bảng quan hệ
3. Lập trình chức năng (MapReduce) thay vì truy vấn khai báo (SQL)
4. Xử lý hàng loạt tự động thay vì giao dịch trực tuyến

---

Большинство объектов физического мира неимоверно сложны по своей организации. Когда мы пытаемся описать какой-либо из таких объектов, мы на самом деле придумываем модель, соответствующую ему в нашем понимании. Если объекты можно поделить на некоторые группы, удовлетворяющие одинаковым моделям, то мы получаем ситуацию, когда внутри базы данных хранятся две группы сущностей:

1. описания моделей объектов;
2. записи, удовлетворяющие какой-либо из моделей и соответствующие различным представителям объектов.

Hầu hết các vật thể trong thế giới vật chất đều có cách tổ chức vô cùng phức tạp. Khi chúng tôi cố gắng mô tả bất kỳ đối tượng nào trong số này, chúng tôi thực sự nghĩ ra một mô hình tương ứng với nó theo cách hiểu của chúng tôi. Nếu các đối tượng có thể được chia thành các nhóm nhất định thỏa mãn các mô hình giống nhau thì chúng ta sẽ gặp tình huống trong đó có hai nhóm thực thể được lưu trữ bên trong cơ sở dữ liệu:

1. mô tả mô hình đối tượng;
2. hồ sơ đáp ứng bất kỳ mô hình nào và tương ứng với các đại diện khác nhau của đối tượng.

---

Но бывают ситуации, когда объекты настолько различны, что их нельзя классифицировать. Тогда база данных представляет из себя набор из одних лишь моделей.

Nhưng có những tình huống khi các đối tượng quá khác nhau đến mức không thể phân loại được. Sau đó, cơ sở dữ liệu là một tập hợp các mô hình duy nhất.

Когда мы говорим о моделях данных, мы должны понимать, что нужно уметь хранить не только сами объекты, но и взаимосвязи между ними. Существует несколько видов взаимосвязей между объектами:

1. один к одному – 1:1;
2. один ко многим – 1:M;
3. многие ко многим – M:M.

Khi nói về mô hình dữ liệu, chúng ta phải hiểu rằng chúng ta cần có khả năng lưu trữ không chỉ bản thân các đối tượng mà còn cả mối quan hệ giữa chúng. Có một số loại mối quan hệ giữa các đối tượng:

1. một đến một – 1:1.
2. một đến nhiều – 1:M.
3. nhiều đến nhiều – M:M.

## Язык SQL

**Язык SQL (Structured Query Language)** – это основной язык взаимодействия с информацией, размещённой в реляционной базе данных. В той или иной модификации язык SQL есть во всех основных СУБД, но для каждой из них характерен свой диалект языка.

**SQL (Ngôn ngữ truy vấn có cấu trúc)** là ngôn ngữ chính để tương tác với thông tin được lưu trữ trong cơ sở dữ liệu quan hệ. Trong bản sửa đổi này hay bản sửa đổi khác, ngôn ngữ SQL có sẵn trong tất cả các DBMS chính, nhưng mỗi cơ sở dữ liệu đều có phương ngữ ngôn ngữ riêng.

Язык SQL позволяет создавать и манипулировать объектами реляционной БД.

Ngôn ngữ SQL cho phép bạn tạo và thao tác các đối tượng cơ sở dữ liệu quan hệ.

Например, SQL позволяет создавать таблицы, модифицировать их, наполнять строками, модифицировать строки, удалять строки и т.д.

Ví dụ: SQL cho phép bạn tạo bảng, sửa đổi chúng, điền các hàng vào chúng, sửa đổi hàng, xóa hàng, v.v.

| Название | Назначение | Примеры команд |
| -------- | ---------- | -------------- |
| DDL (Data Definition Language) | Набор действий языка SQL, отвечающих за определение данных. То есть команды создания/удаления/модификации объектов. Например, таблиц. | CREATE TABLE, DROP TABLE, ALTER TABLE, RENAME TABLE |
| DML (Data Manipulation Language) | Набор действий языка SQL, отвечающих за манипуляцию с данными. То есть команды, отвечающие за наполнение объектов или выборку из них. Например, добавление, удаление, выборка или модификация строк таблиц. | SELECT, INSERT, UPDATE, DELETE |
| DCL (Data Control Language) | Набор действий языка SQL, отвечающих за разграничение прав доступ. Например, разрешение на выборку строк из таблицы. | GRANT, REVOKE |
