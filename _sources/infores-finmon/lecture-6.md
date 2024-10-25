# Глава 6. Поисковые задачи, средства и технологии информационного поиска

Эпиграфом к этой и следующей главе могли бы быть тезисы, сформулирован-ные на заре АИПС: «До тех пор, пока люди не научатся адекватно выражать на есте-ственном языке свои информационные потребности, документальная ИПС должна быть организована таким образом, чтобы человек мог как бы исследовать поисковый массив, изменяя формулировку поискового предписания в зависимости от промежу-точных результатов поиска. По-видимому, единственная возможность хотя бы частич-ного решения проблемы неадекватности словесного выражения информационных по-требностей ученых и инженеров пока состоит в конструировании документальных ИПС как систем класса «человек—машина»» [Михайлов, 1968].

Phần ngoại văn của chương này và chương tiếp theo có thể được xây dựng vào thời kỳ đầu của AIPS: “Cho đến khi mọi người học cách diễn đạt đầy đủ nhu cầu thông tin của họ bằng ngôn ngữ tự nhiên, IPS tài liệu phải được tổ chức theo cách mà một người có thể khám phá mảng tìm kiếm , thay đổi cách diễn đạt của hướng dẫn tìm kiếm tùy thuộc vào kết quả tìm kiếm trung gian. Rõ ràng, khả năng duy nhất để giải quyết ít nhất một phần vấn đề về sự bất cập trong việc diễn đạt bằng lời về nhu cầu thông tin của các nhà khoa học và kỹ sư cho đến nay là xây dựng các hệ thống thông tin tài liệu như các hệ thống thuộc lớp “người-máy”” [Mikhailov, 1968].

---

В задачах информационного поиска качественно различают две составляющие: **концептуальную** и **технологическую**.

Trong các nhiệm vụ truy xuất thông tin, hai thành phần được phân biệt về mặt chất lượng: **khái niệm** và **công nghệ**.

---

К концептуальным составляющим относятся, прежде всего, методы и средства представления собственно информации и метаинформации, которые используются в качестве основы как для проектирования механизма поиска, так и для организации процессов взаимодействия пользователя с АИПС.

Các thành phần khái niệm trước hết bao gồm các phương pháp và phương tiện trình bày thông tin thực tế và siêu thông tin, được sử dụng làm cơ sở cho cả việc thiết kế cơ chế tìm kiếm và tổ chức các quá trình tương tác của người dùng với AIPS.

---

К технологическим составляющим относятся средства пользовательского ин-терфейса, алгоритмы индексирования и поиска, языки запросов, средства интеграции информации из различных источников и т. д.

Các thành phần công nghệ bao gồm các công cụ giao diện người dùng, thuật toán lập chỉ mục và tìm kiếm, ngôn ngữ truy vấn, phương tiện tích hợp thông tin từ nhiều nguồn khác nhau, v.v.

---

Принципиально важным фактором, определяющим направление развития со-временных информационных систем, является то, что взаимодействие пользователей с информационными ресурсами происходит в режиме «информационного самообслужи-вания», когда пользователь, по существу, уже не разделяет свою деятельность на ин-формационную и основную1. Отметим также, что для пользователей - профессионалов в своей области, характерна тематическая устойчивость интересов, а в том случае, если они являются «информационно-ориентированными», то им обыкновенно свойственно желание и способность организовать информационное пространство своей предметной области в своей вычислительной среде. Это означает, что в процессе поиска пользова-тель фактически создает новый проблемно-ориентированный информационный ресурс, им самим формируемый и систематизируемый, который может включать помимо под-борок документов также и метаинформацию, например словари специальной термино-логии, классификаторы предметных областей, описания ресурсов и т. д.

Yếu tố cơ bản quan trọng quyết định hướng phát triển của hệ thống thông tin hiện đại là sự tương tác của người dùng với tài nguyên thông tin xảy ra ở chế độ “tự phục vụ thông tin”, khi về bản chất, người dùng không còn phân chia hoạt động của mình thành thông tin và cơ bản1. Chúng tôi cũng lưu ý rằng những người dùng là chuyên gia trong lĩnh vực của họ được đặc trưng bởi sự ổn định về chủ đề và nếu họ là người “định hướng thông tin” thì họ thường có mong muốn và khả năng tổ chức không gian thông tin về lĩnh vực chủ đề của họ trong môi trường máy tính của họ. . Điều này có nghĩa là trong quá trình tìm kiếm, người dùng thực sự tạo ra một nguồn thông tin mới hướng đến vấn đề, do chính họ hình thành và hệ thống hóa, có thể bao gồm, ngoài các bộ sưu tập tài liệu, còn có siêu thông tin, chẳng hạn như từ điển thuật ngữ đặc biệt , phân loại các lĩnh vực chủ đề, mô tả các nguồn tài nguyên, v.v.

---

Особенности технических решений при проектировании и эксплуатации АИС, ориентированных на информационную поддержку основной деятельности и интегри-рующих такие функции, как поиск, обработка и организация информации, определяют-ся двумя следующими, имеющими разную природу факторами.

1. Используемые информационные ресурсы, наряду с оригинальным авторским представлением материала, в большинстве своем характеризуются высокой системати-зированностью (тематической профильностью источников и ядерностью тематических потоков), а также практически обязательным наличием справочной информации (поис-ковых образов документов и систем вторичной информации – рубрикаторов и тезауру-сов, обеспечивающих единообразие представления и организации доступа к ресурсам).
2. Поисковые средства и технологии, используемые для реализации информаци-онных потребностей, определяются типом и состоянием решаемой пользователем задачи основной деятельности: соотношением его знания и незнания об исследуемом объ-екте. Кроме того, процесс взаимодействия пользователя с системой определяется уров-нем его знания о содержании ресурса (полноты представления, достоверности источни-ка и т.д.) и функциональных возможностях системы как инструмента. В целом эти фак-торы обычно сводятся к понятию «профессионализма» – информационного (подготов-ленный/неподготовленный пользователь ИР) и предметного (профессио-нал/непрофессионал в сфере ОД).

Đặc điểm của giải pháp kỹ thuật trong thiết kế và vận hành hệ thống thông tin tự động, tập trung vào hỗ trợ thông tin cho các hoạt động cốt lõi và tích hợp các chức năng như tìm kiếm, xử lý và tổ chức thông tin, được xác định bởi hai yếu tố có tính chất khác nhau sau đây.

1. Các nguồn thông tin được sử dụng, cùng với cách trình bày tài liệu của tác giả ban đầu, hầu hết có đặc điểm là tính hệ thống hóa cao (hồ sơ chuyên đề của các nguồn và tính chất cốt lõi của các chủ đề theo chủ đề), cũng như sự hiện diện gần như bắt buộc của thông tin tham khảo (tìm kiếm hình ảnh của tài liệu và hệ thống thông tin thứ cấp - bảng đánh giá và từ điển đồng nghĩa, đảm bảo tính thống nhất trong cách trình bày và tổ chức tiếp cận nguồn tài liệu).
2. Các công cụ và công nghệ tìm kiếm được sử dụng để đáp ứng nhu cầu thông tin được xác định bởi loại và trạng thái của vấn đề hoạt động chính mà người dùng đang giải quyết: tỷ lệ giữa kiến ​​thức và sự thiếu hiểu biết của họ về đối tượng đang nghiên cứu. Ngoài ra, quá trình tương tác của người dùng với hệ thống được xác định bởi mức độ hiểu biết của anh ta về nội dung của tài nguyên (tính đầy đủ của cách trình bày, độ tin cậy của nguồn, v.v.) và chức năng của hệ thống như một công cụ. Nhìn chung, các yếu tố này thường bắt nguồn từ khái niệm “tính chuyên nghiệp” - thông tin (người dùng IR được đào tạo/chưa qua đào tạo) và chủ đề (chuyên nghiệp/không chuyên nghiệp trong lĩnh vực OA).

## 6.1. Информационные объекты в совокупной системе основной и информа-ционной деятельности

> 6.1. Các đối tượng thông tin trong tổng thể hệ thống hoạt động cơ bản và thông tin

С методологической точки зрения взаимодействие пользователя с комплексом разнородных ИР должно рассматриваться как процесс, зависящий от двух групп основ-ных факторов. С одной стороны – это свойства информации и закономерности инфор-мационных преобразований в сфере основной деятельности, в том числе в процессе ге-нерации новой информации. С другой стороны, организация информационного про-странства должна рассматриваться как задача такого управления ресурсами, при кото-ром информационная система пользователя позволяла бы ему работать с ними как с единым ресурсом. Кроме того, технологии взаимодействия должны учитывать специ-фику восприятия и переработки человеком как основной (целевой) информации, так и информационно-технологической, регулирующей условия его взаимодействия с ин-формационной средой.

Từ quan điểm phương pháp luận, sự tương tác của người dùng với một tổ hợp IR không đồng nhất nên được coi là một quá trình phụ thuộc vào hai nhóm yếu tố chính. Một mặt, đây là những đặc tính của thông tin và mô hình biến đổi thông tin trong lĩnh vực hoạt động cốt lõi, bao gồm cả quá trình tạo ra thông tin mới. Mặt khác, việc tổ chức không gian thông tin phải được coi là nhiệm vụ quản lý tài nguyên theo cách mà hệ thống thông tin của người dùng cho phép họ làm việc với chúng như một tài nguyên duy nhất. Ngoài ra, các công nghệ tương tác phải tính đến các đặc điểm cụ thể trong nhận thức và xử lý của con người về cả thông tin cơ bản (mục tiêu) và công nghệ thông tin điều chỉnh các điều kiện tương tác của anh ta với môi trường thông tin.

---

Рассмотрим обобщенную схему воспроизводства информации, в основу которой положено описанное во второй главе представление совокупной информационной си-стемы (генератор – потребитель информации), связывающей объекты и процессы ос-новной и собственно информационной деятельности (рис. 6.1).

Chúng ta hãy xem xét một sơ đồ tổng quát để tái tạo thông tin, dựa trên cách biểu diễn hệ thống thông tin tổng hợp (người tạo - người tiêu dùng thông tin) được mô tả trong chương thứ hai, kết nối các đối tượng và quy trình của hoạt động thông tin chính và thực tế (Hình 6.1).

---

С точки зрения задач управления потоками здесь можно различить две совокуп-ности процессов: формирование потока информации (документов) в соответствии с заданными характеристиками (тематичность, полнота охвата и т. д.) и распределение входных и выходных потоков и их составляющих в соответствии с информационными потребностями2. Соответственно, если основная деятельность имеет дело с поиском и содержательной обработкой информации (т. е. сообщениями, описывающими некото-рые свойства исследуемого объекта), то научно-информационная – это по возможности инвариантные относительно смысла преобразования текста в форму, приемлемую для автоматизированной идентификации, хранения и поиска.

Từ quan điểm của nhiệm vụ quản lý luồng, có thể phân biệt hai nhóm quy trình ở đây: hình thành luồng thông tin (tài liệu) theo các đặc điểm nhất định (nội dung chủ đề, mức độ bao phủ đầy đủ, v.v.) và phân phối đầu vào và các luồng đầu ra cũng như các thành phần của chúng phù hợp với nhu cầu thông tin2. Theo đó, nếu hoạt động chính liên quan đến việc tìm kiếm và xử lý thông tin có ý nghĩa (tức là các thông điệp mô tả một số thuộc tính của đối tượng đang nghiên cứu), thì hoạt động thông tin khoa học, nếu có thể, là bất biến đối với ý nghĩa của việc chuyển đổi văn bản thành một hình thức được chấp nhận để nhận dạng, lưu trữ và tìm kiếm tự động.

---

По характеру преобразований информации в совокупной системе (рис. 6.1) можно выделить, как ранее отмечалось, три следующих уровня.

Dựa trên bản chất của sự biến đổi thông tin trong hệ thống tổng hợp (Hình 6.1), chúng ta có thể phân biệt, như đã lưu ý trước đó, ba cấp độ sau.

**Первый уровень** – это основная деятельность, где объектами являются предметы реального мира, а результатами – новое знание. Носителем информации этого уровня является человеческое сознание, для которого характерны системность организации и ассоциативность выборки, а коммуникационным объектом является сообщение – зна-ние, адресно отраженное на систему понятий предполагаемого приемника-потребителя информации.

**Cấp độ đầu tiên** là hoạt động chính, trong đó đối tượng là đối tượng của thế giới thực và kết quả là kiến ​​thức mới. Người mang thông tin ở cấp độ này là ý thức của con người, được đặc trưng bởi tổ chức có hệ thống và lấy mẫu liên kết, và đối tượng giao tiếp là một thông điệp - kiến ​​thức, hướng đến hệ thống các khái niệm của người tiêu dùng thông tin dự kiến.

**Второй уровень** – создание общественно-полезной информации – одна из форм овеществления знаний через обобществление результатов, обычно, в документальной форме. Средством представления знаний здесь является язык, а носителем – документ как функционально ориентированное сообщение, структурирующее информацию и идентифицирующее ее, например, путем выделения логических или физических частей – семантически однородных полей.

**Cấp độ thứ hai** - tạo ra thông tin hữu ích cho xã hội - một trong những hình thức hiện thực hóa kiến ​​thức thông qua xã hội hóa kết quả, thường ở dạng tài liệu. Phương tiện biểu diễn kiến ​​thức ở đây là ngôn ngữ, và vật mang là một tài liệu như một thông điệp định hướng chức năng, cấu trúc thông tin và xác định nó, chẳng hạn, bằng cách làm nổi bật các phần logic hoặc vật lý - các trường đồng nhất về mặt ngữ nghĩa.

**Третий уровень** – собственно информационная деятельность – управление пото-ками информации для обеспечения основной деятельности. Работа с компактными по объему вторичными документами, позволяет совершенствовать процесс поиска нуж-ных сообщений. Здесь информация (поисковый образ документа) – это хорошо струк-турированный материал, компактно и системно отражающий содержание документа, а также обеспечивающий идентифицируемость документа как в целом, так и на уровне отдельных элементов данных.

**Cấp độ thứ ba** – bản thân hoạt động thông tin – quản lý các luồng thông tin để hỗ trợ các hoạt động cốt lõi. Làm việc với các tài liệu thứ cấp nhỏ gọn cho phép bạn cải thiện quá trình tìm kiếm các thông báo cần thiết. Ở đây, thông tin (hình ảnh tìm kiếm của tài liệu) là một tài liệu có cấu trúc tốt, phản ánh một cách cô đọng và có hệ thống nội dung của tài liệu, đồng thời đảm bảo khả năng nhận dạng của tài liệu cả về tổng thể lẫn ở cấp độ các thành phần dữ liệu riêng lẻ.

---

```{figure} 6-1.png
Рис. 6.1. Обобщенная схема воспроизводства информации
```

---

Для выявления характера взаимосвязи информационных объектов разных уров-ней используем приведенное в гл. 1 определение понятия «информация» как отражения и, соответственно, ограничения разнообразия описаний объектов ОД и их взаимосвязей в соответствии с возможностями средств представления (языка описания). Отсюда сле-дует, что использование абстракций различного порядка в итоге дает возможность (упрощая описание объекта одного семантического уровня за счет введения объектов другого уровня) представлять объекты с помощью конечного числа терминов. Соотно-шение и характер взаимосвязей информационных объектов, форм их представления, рассматриваемых в контексте задач информационного обеспечения основной деятель-ности, приведены на рис. 6.2.

Để xác định bản chất của mối quan hệ giữa các đối tượng thông tin ở các cấp độ khác nhau, chúng tôi sử dụng những gì được đưa ra trong Chương. 1 định nghĩa về khái niệm “thông tin” như một sự phản ánh và theo đó, giới hạn tính đa dạng của các mô tả đối tượng OA và các mối quan hệ của chúng phù hợp với khả năng của các phương tiện trình bày (ngôn ngữ mô tả). Theo đó, việc sử dụng sự trừu tượng hóa của các trật tự khác nhau cuối cùng làm cho nó có thể (bằng cách đơn giản hóa việc mô tả một đối tượng ở một cấp độ ngữ nghĩa bằng cách đưa vào các đối tượng ở một cấp độ khác) để biểu diễn các đối tượng bằng cách sử dụng một số lượng hữu hạn các thuật ngữ. Mối tương quan và bản chất của mối tương quan giữa các đối tượng thông tin, các hình thức biểu diễn của chúng, được xem xét trong bối cảnh nhiệm vụ hỗ trợ thông tin của hoạt động chính, được thể hiện trong Hình 6.2.

---

Здесь преобразование форм представления информации является последова-тельным отражением содержания, а по существу – фильтрацией информации путем снижения разнообразия форм и аспектов представления смыслового содержания через вынесение части смысла в метаинформационную составляющую или простым отбра-сыванием. Например, сообщение предполагает фиксацию (ограничение) предметной области; документ – фиксацию вариантов способа представления через выделение се-мантически однородных полей и, соответственно, определение характера и способа их наполнения; поисковый образ фиксирует способы указания значения отдельного эле-мента (типа данных).

Ở đây, việc chuyển đổi các hình thức trình bày thông tin là sự phản ánh nhất quán về nội dung và về bản chất - là sự lọc thông tin bằng cách giảm bớt sự đa dạng của các hình thức và khía cạnh của việc trình bày nội dung ngữ nghĩa thông qua việc chuyển một phần ý nghĩa sang meta -thành phần thông tin hoặc loại bỏ đơn giản. Ví dụ: thông báo ngụ ý sự cố định (giới hạn) của lĩnh vực chủ đề; tài liệu - cố định các tùy chọn cho phương pháp trình bày thông qua việc lựa chọn các trường đồng nhất về mặt ngữ nghĩa và theo đó, xác định tính chất và phương pháp điền chúng; hình ảnh tìm kiếm ghi lại các cách chỉ định giá trị của một phần tử riêng lẻ (kiểu dữ liệu).

---

Соответственно, адекватность средств отражения информации (а в случае ИПС – это средства лингвистического обеспечения) должна рассматриваться как с точки зрения возможности неискажающего преобразования самой информации в цепи гене-рации-потребления информационного ресурса, так и с точки зрения адекватности вос-приятия пользователем функциональных возможностей этих средств.

Theo đó, tính đầy đủ của các phương tiện phản ánh thông tin (và trong trường hợp các hệ thống truy xuất thông tin, đây là các phương tiện hỗ trợ ngôn ngữ) cần được xem xét cả từ quan điểm về khả năng chuyển đổi không làm sai lệch bản thân thông tin trong ngôn ngữ. chuỗi tạo và tiêu thụ một nguồn tài nguyên thông tin và từ quan điểm về mức độ nhận thức đầy đủ của người dùng về chức năng của các quỹ này.

```{figure} 6-2.png
Рис. 6.2. Уровневая модель взаимосвязи информационных объектов
```

## 6.2. Поисковые задачи и виды информационного поиска

Как было показано ранее, особенностью поискового процесса, рассматриваемого как взаимодействие двух систем представления знаний (пользователь – АИПС), является многоуровневость и неоднородность объектов в цепи информационных преобразований.

Như đã trình bày trước đó, một đặc điểm của quá trình tìm kiếm, được coi là sự tương tác của hai hệ thống biểu diễn tri thức (người dùng - AIPS), là tính đa cấp và không đồng nhất của các đối tượng trong chuỗi biến đổi thông tin.

### 6.2.1. Типология поисковых задач

Операционными объектами, непосредственно участвующими во взаимодействии (сравнении потребности и документов в БД), являются поисковый образ документа (ПОД) и поисковый образ запроса (ПОЗ), формальное соответствие которых устанавливается поисковым механизмом АИПС. Для установления же соответствия содержания на смысловом уровне пользователь должен реконструировать (возможное!) содержание по перечислению основных понятий и далее полученный образ соотносит с реальной потребностью. При этом адекватность образа действительному содержанию документа определяется не только качеством процесса свертки информации, но и уровнем знания субъектом средств отражения – концептуальной схемы предметной области и возможностей ИПЯ.

Các đối tượng hoạt động liên quan trực tiếp đến sự tương tác (so sánh nhu cầu và tài liệu trong cơ sở dữ liệu) là hình ảnh tìm kiếm của tài liệu (SID) và hình ảnh tìm kiếm của yêu cầu (SRE), sự tương ứng chính thức được thiết lập bởi cơ chế tìm kiếm của AIPS. Để thiết lập sự tương ứng của nội dung ở cấp độ ngữ nghĩa, người dùng phải xây dựng lại nội dung (có thể!) bằng cách liệt kê các khái niệm cơ bản và sau đó đối chiếu hình ảnh thu được với nhu cầu thực sự. Đồng thời, mức độ phù hợp của hình ảnh với nội dung thực tế của tài liệu không chỉ được quyết định bởi chất lượng của quá trình tích chập thông tin mà còn bởi trình độ hiểu biết của chủ thể về các phương tiện phản ánh - sơ đồ khái niệm của chủ thể. khu vực và khả năng của FL.

---

По характеру и степени соотношения в предмете поиска известного и неизвестного (как степени семантической неопределенности) можно выделить три типа поисковых задач.

Dựa trên tính chất và mức độ tương quan trong chủ đề tìm kiếm giữa cái đã biết và cái chưa biết (như mức độ không chắc chắn về ngữ nghĩa), có thể phân biệt ba loại nhiệm vụ tìm kiếm.

---

К задачам первого типа (так называемый предметный, или атрибутивный вид поиска) относится поиск объекта, когда известно, что этот объект существует (например, поиск фактографии или трудов конкретного автора). Поисковая модель (логическая идентификация объекта поиска) может быть представлена как поиск по атрибутам. Для документального поиска – это отбор по логическому выражению над именами понятий, задаваемыми терминами или их комбинациями.

Các nhiệm vụ của loại đầu tiên (cái gọi là loại tìm kiếm chủ đề hoặc thuộc tính) bao gồm tìm kiếm một đối tượng khi biết rằng đối tượng này tồn tại (ví dụ: tìm kiếm thông tin thực tế hoặc tác phẩm của một tác giả cụ thể). Mô hình tìm kiếm (nhận dạng logic của đối tượng tìm kiếm) có thể được biểu diễn dưới dạng tìm kiếm theo thuộc tính. Đối với tìm kiếm tài liệu, đây là sự lựa chọn bằng biểu thức logic đối với tên của các khái niệm được chỉ định bởi các thuật ngữ hoặc sự kết hợp của chúng.

---

Второй тип задач (так называемый тематический вид поиска) – подбор информации по некоторой теме, например, для обзора научной проблемы, обоснования или поиска метода решения практической задачи. Тематический поиск – это нахождение в среде ИС описаний актуально существующих в ПрО основной деятельности объектов, свойства которых могут быть полностью определены на уже известном множестве атрибутов. Неопределенность отображения объекта на предметную область ИС порождается возможной множественностью системного основания на уровне среды ИС. Поисковая модель в этом случае – это поиск по части известного понятия или связям, частично задаваемым комбинацией характеристических признаков. Тематический поиск реализуется как последовательность атрибутивных поисков, каждый из которых соответствует определенному (априорно заданному) системному основанию представления объекта поиска.

Loại nhiệm vụ thứ hai (còn gọi là loại tìm kiếm theo chủ đề) là lựa chọn thông tin về một chủ đề nhất định, chẳng hạn như xem xét một vấn đề khoa học, chứng minh hoặc tìm kiếm phương pháp giải quyết một vấn đề thực tế. Tìm kiếm theo chủ đề là việc khám phá trong môi trường IS các mô tả về các đối tượng thực sự tồn tại trong SbA của hoạt động chính, các thuộc tính của chúng có thể được xác định hoàn toàn trên một tập hợp các thuộc tính đã biết. Sự không chắc chắn của việc ánh xạ một đối tượng vào một vùng chủ đề IS được tạo ra bởi khả năng có nhiều nền tảng hệ thống ở cấp độ môi trường IS. Mô hình tìm kiếm trong trường hợp này là tìm kiếm một phần của khái niệm hoặc các kết nối đã biết, được xác định một phần bằng sự kết hợp của các đặc điểm đặc trưng. Tìm kiếm theo chủ đề được triển khai dưới dạng một chuỗi các tìm kiếm thuộc tính, mỗi tìm kiếm tương ứng với một cơ sở hệ thống cụ thể (được chỉ định trước) để thể hiện đối tượng tìm kiếm.

---

Третий тип задач представляет собой вид проблемного поиска, который, по сути, является основной составляющей творческого процесса – определения путей решения профессиональной задачи пользователя. Проблемный поиск – это нахождение в ИСр описаний объектов или их составляющих, потенциально существующих в ПрО основной деятельности, и в совокупности, возможно, образующих целое, свойства которого будут больше суммы свойств частей. То есть, этим свойствам в явной форме не соответствуют «собственные» атрибуты, а новое свойство, например, может быть задано комбинацией уже известных атрибутов. В этом случае к неопределенности отображения объекта на предметную область ИС, свойственной тематическому поиску, добавляется неопределенность представления объекта на уровне «субъект-объект ОД»: представление, которое субъект имеет об объекте, может не соответствовать реальности. Логическая поисковая модель для этого случая – поиск «похожих» документов, содержание которых некоторым образом ассоциируется с задачей пользователя.

Loại nhiệm vụ thứ ba là loại tìm kiếm vấn đề, trên thực tế, là thành phần chính của quá trình sáng tạo - xác định cách giải quyết vấn đề chuyên môn của người dùng. Tìm kiếm có vấn đề là việc tìm thấy trong IS các mô tả về đối tượng hoặc các thành phần của chúng có khả năng tồn tại trong SbA của hoạt động chính và trong tổng hợp, có thể tạo thành một tổng thể, các thuộc tính của nó sẽ lớn hơn tổng các thuộc tính của các bộ phận. Nghĩa là, các thuộc tính này không tương ứng rõ ràng với các thuộc tính “của riêng” và chẳng hạn, một thuộc tính mới có thể được chỉ định bằng cách kết hợp các thuộc tính đã biết. Trong trường hợp này, đối với sự không chắc chắn của việc ánh xạ một đối tượng vào một vùng chủ đề IS, đặc điểm của tìm kiếm theo chủ đề, được bổ sung thêm độ không chắc chắn của việc biểu diễn một đối tượng ở cấp độ “chủ thể-đối tượng OA”: ý tưởng mà một chủ thể có về một đối tượng có thể không tương ứng với thực tế. Mô hình tìm kiếm hợp lý cho trường hợp này là tìm kiếm các tài liệu “tương tự”, nội dung của chúng theo một cách nào đó được liên kết với nhiệm vụ của người dùng.

---

С точки зрения структурной полноты определения поискового объекта типоло-гия видов поиска (соответственно типам поисковых задач) представлена в табл. 6.1.

Từ quan điểm về tính đầy đủ về mặt cấu trúc của định nghĩa đối tượng tìm kiếm, kiểu chữ của các loại tìm kiếm (theo loại nhiệm vụ tìm kiếm) được trình bày trong Bảng. 6.1.

---

Таблица 6.1. Типология видов поиска

| Вид поиска | Логическая модель объекта поиска | Логическая модель механизма поиска |
| --- | --- | --- |
| Предметный (атрибутивный) поиск | Объем понятия, задаваемого именем | Поиск по логическому выражению над име-нами понятий, задаваемыми терминами или их комбинацией (значениями определенного характеристического признака) |
| Тематический поиск | Определение нового понятия или по-нятийных связей, косвенно опреде-ленного объемом этого понятия | Поиск по части известного понятия (или свя-зям), частично задаваемого комбинацией ха-рактеристических признаков, с использова-нием накопленных ранее результатов |
| Проблемный по-иск | Документальное определение нового понятия или связей путем реконструк-ции образа по его части | Поиск «похожих» документов, поиск с ис-пользованием технологии «обратной связи» |

---

Типология видов поиска может быть представлена и с точки зрения семиотики как знаковой системы, которой свойственна неизоморфность отображения системы обозначающих (знаков) системе обозначаемых (объектов-денотатов). Приведенная вы-ше типология ассоциируется со следующими семиотическими ситуациями.

Kiểu chữ của các loại tìm kiếm cũng có thể được trình bày từ quan điểm ký hiệu học như một hệ thống ký hiệu, được đặc trưng bởi sự ánh xạ không đẳng cấu của hệ thống các ký hiệu (dấu hiệu) sang hệ thống các ký hiệu (đối tượng biểu thị). Kiểu chữ trên gắn liền với các tình huống ký hiệu học sau đây.

---

Предметному поиску соответствует ситуация формирования (выбора) знака (конструкции), устраняющего неопределенность знаковой системы, т. е. определение такого знака (термина), который позволит эффективно выделить (отличить) объект из множества других при фиксированном (единственном) концепте. Этот случай иллю-стрируется рис. 6.3, а.

Tìm kiếm chủ đề tương ứng với tình huống hình thành (chọn lọc) một dấu hiệu (xây dựng) loại bỏ tính không chắc chắn của hệ thống dấu hiệu, tức là xác định một dấu hiệu (thuật ngữ) sẽ phân biệt (phân biệt) một cách hiệu quả một đối tượng với nhiều đối tượng khác bằng một điểm cố định (duy nhất) ý tưởng. Trường hợp này được minh họa trong hình. 6.3, a.

```{figure} 6-3.png
Рис. 6.3. Семиотические ситуации поиска
```

Для случая тематического поиска ситуация отличается тем, что мы имеем упо-рядоченное ограниченное множество концептов, позволяющих представлять объект в различных аспектах, что представлено на рис. 6.3, b.

Đối với trường hợp tìm kiếm theo chủ đề, tình huống khác ở chỗ chúng ta có một tập hợp các khái niệm có trật tự, giới hạn cho phép chúng ta biểu diễn đối tượng theo nhiều khía cạnh khác nhau, như trong Hình 6.3, b.

---

Для случая проблемного поиска мы уже имеем неупорядоченное и нечетко опре-деленное множество концептов.

Đối với trường hợp tìm kiếm có vấn đề, chúng ta đã có sẵn một tập hợp các khái niệm không có thứ tự và được xác định một cách mơ hồ.

### 6.2.2. Типология информационной неопределенности

Особенности представления информации на разных уровнях человеко-машинной среды обусловливают различные типы неопределенности – семантическую, лингвистическую, метаинформационную (последняя относится как к семантике, так и к синтаксису представления информации).

Các đặc điểm của việc trình bày thông tin ở các cấp độ khác nhau của môi trường con người-máy xác định các loại độ không chắc chắn khác nhau - ngữ nghĩa, ngôn ngữ, siêu thông tin (cái sau liên quan đến cả ngữ nghĩa và cú pháp trình bày thông tin).

---

В этом смысле процесс поиска можно определить как последовательность шагов, задачи которых – снятие перечисленных неопределенностей.

Theo nghĩa này, quá trình tìm kiếm có thể được định nghĩa là một chuỗi các bước có nhiệm vụ loại bỏ những điều không chắc chắn được liệt kê.

---

Семантическая неопределенность связана с формализацией запроса. Формируя запрос, пользователь явно или неявно синтезирует ту информацию, которая, возможно, есть в отыскиваемом тексте. Определяются понятия и связи между ними, т.е. происходит реконструкция пользователем гипотетического текста, предположительно совпадающего в известной части проблемы с возможно уже существующим текстом, и обозначение связи известного знания с выявленным неизвестным.

Sự không chắc chắn về mặt ngữ nghĩa có liên quan đến việc chính thức hóa yêu cầu. Khi hình thành một truy vấn, người dùng sẽ tổng hợp rõ ràng hoặc ngầm thông tin có thể có trong văn bản đang được tìm kiếm. Các khái niệm và mối liên hệ giữa chúng được xác định, tức là người dùng xây dựng lại một văn bản giả định được cho là trùng khớp ở phần đã biết của vấn đề với một văn bản có thể đã tồn tại và chỉ ra mối liên hệ giữa kiến ​​thức đã biết và cái chưa biết đã xác định.

---

Лингвистическая (лексическая) неопределенность связана с формулировкой ПОЗ. Формулируя запрос, пользователь должен учитывать, что его представление об информативности термина необязательно совпадает с представлениями индексатора. Для ИПЯ дескрипторного типа с простой грамматикой это в значительной степени сводится к лексической неопределенности.

Sự không chắc chắn về ngôn ngữ (từ vựng) có liên quan đến việc xây dựng POS. Khi xây dựng một truy vấn, người dùng phải tính đến việc ý tưởng của mình về nội dung thông tin của một thuật ngữ không nhất thiết trùng với ý tưởng của người lập chỉ mục. Đối với FL kiểu mô tả có ngữ pháp đơn giản, điều này phần lớn dẫn đến sự mơ hồ về từ vựng.

---

Метаинформационная неопределенность связана с тем, что пользователь должен иметь адекватное представление о самой системе и способе представления информации в ней. Например, как и по каким полям проводить поиск.

Sự không chắc chắn về siêu thông tin có liên quan đến thực tế là người dùng phải có hiểu biết đầy đủ về bản thân hệ thống và cách trình bày thông tin trong đó. Ví dụ: tìm kiếm bằng cách nào và theo trường nào.

---

Рассмотрим человеко-машинный поиск информации как процесс отыскания не-известных (по крайней мере, для субъекта поиска) сведений (фактов, идей и т. д.), не-обходимых для получения знания, нового для данной предметной области (например, позволяющего выявить связи между фрагментами известного знания или найти приме-ры, опровергающие научные гипотезы).

Chúng ta hãy coi tìm kiếm thông tin con người-máy là một quá trình tìm kiếm thông tin chưa biết (ít nhất là đối với chủ đề tìm kiếm) (sự kiện, ý tưởng, v.v.) cần thiết để có được kiến ​​thức mới cho một lĩnh vực chủ đề nhất định (ví dụ: cho phép để xác định mối liên hệ giữa các mảnh kiến ​​thức đã biết hoặc tìm các ví dụ bác bỏ các giả thuyết khoa học).

---

Такой процесс характеризуется двойственностью целей человека. С одной сто-роны – это создание нового знания, включая этапы структуризации и формализации проблемы, нахождения или разработки методов решения. С другой стороны – это поиск сообщений и оценка полезности найденного.

Quá trình này được đặc trưng bởi tính hai mặt của các mục tiêu của con người. Một mặt, đây là hoạt động tạo ra tri thức mới, bao gồm các khâu cấu trúc và hình thức hóa vấn đề, tìm kiếm hoặc phát triển các phương pháp giải quyết. Mặt khác, nó đang tìm kiếm các thông điệp và đánh giá tính hữu ích của những gì được tìm thấy.

---

Столь же значимой особенностью поисковой ситуации является опосредован-ность отбора информации, материально представленной в виде документов. Потенци-ально полезные документы (предположительно содержащие нужные сведения) выде-ляются из всего доступного множества через соотнесение поисковых образов (инфор-мационной потребности и содержания документа, выраженных средствами ИПЯ).

Một đặc điểm quan trọng không kém của tình huống tìm kiếm là tính chất gián tiếp của việc lựa chọn thông tin, được trình bày một cách vật chất dưới dạng tài liệu. Các tài liệu có thể hữu ích (có lẽ chứa các thông tin cần thiết) được xác định từ toàn bộ tập hợp có sẵn thông qua sự tương quan của các hình ảnh tìm kiếm (nhu cầu thông tin và nội dung tài liệu, được thể hiện bằng FP).

---

Аналогичная опосредованность наблюдается в случае рассмотрения сред пред-ставления информации: смысловая обработка (соотнесение содержания сообщения с реальной, т. е. осознанной потребностью) происходит в сознании человека, а отбор до-кументов, формально соответствующих потребности, – в машинной среде с жесткой двоичной логикой. Причем такая схема установления соответствия (отражения) по-строена на сведении информационной потребности (как неопределенности и неизвест-ности) к перечислительной форме гипотетически известного, представляющей по-требность гипотетическими документами. Этот прием обеспечивает однородность со-поставляемых поисковых образов и применим, в том числе, и к наиболее распростра-ненным видам информационного поиска, например, библиографическому или отыска-нию публикаций об объектах, уже существующих, так или иначе известных субъекту.

Một tính gián tiếp tương tự được quan sát thấy trong trường hợp xem xét phương tiện trình bày thông tin: quá trình xử lý ngữ nghĩa (tương quan nội dung của thông điệp với nhu cầu thực tế, tức là có ý thức) xảy ra trong tâm trí con người và việc lựa chọn các tài liệu chính thức tương ứng với nhu cầu xảy ra. trong môi trường máy có logic nhị phân cứng nhắc. Hơn nữa, một sơ đồ thiết lập sự tương ứng (phản ánh) như vậy dựa trên việc giảm nhu cầu thông tin (dưới dạng không chắc chắn và chưa biết) thành dạng liệt kê của những gì đã biết theo giả thuyết, thể hiện nhu cầu bằng các tài liệu giả định. Kỹ thuật này đảm bảo tính đồng nhất của các hình ảnh tìm kiếm được so sánh và có thể áp dụng, trong số những thứ khác, cho các loại tìm kiếm thông tin phổ biến nhất, ví dụ: thư mục hoặc tìm kiếm các ấn phẩm về các đối tượng đã tồn tại, theo cách này hay cách khác mà chủ đề đã biết.

---

Такой подход позволяет рассматривать процесс взаимодействия как последова-тельное изменение состояний (этапов) взаимодействующих подсистем (человека и АИПС), направленное на последовательную локализацию неопределенностей следую-щих видов:

1) неопределенности соотношения «известного/неизвестного» в предмете поис-ка;
2) неопределенности системы характеристических признаков для структуриза-ции предмета поиска;
3) семантической неопределенности формулировки предмета поиска;
4) лексической неопределенности как фактора степени соответствия ИПЯ язы-ку предметной области;
5) неопределенности критериев сравнения поисковых образов (адекватность формальных мер близости, реализованных в конкретных АИПС);
6) неопределенности интерпретации ПОЗ (субъективность и неполнота рекон-струирования пользователем смысла найденных документов).

Cách tiếp cận này cho phép chúng tôi coi quá trình tương tác là một sự thay đổi tuần tự về trạng thái (giai đoạn) của các hệ thống con tương tác (con người và AIPS), nhằm mục đích định vị nhất quán các điểm không chắc chắn của các loại sau:

1) sự không chắc chắn của tỷ lệ “đã biết/chưa biết” trong chủ đề tìm kiếm;
2) sự không chắc chắn của hệ thống các đặc điểm đặc trưng để cấu trúc đối tượng tìm kiếm;
3) sự không chắc chắn về ngữ nghĩa trong việc xây dựng chủ đề tìm kiếm;
4) sự không chắc chắn về mặt từ vựng như một yếu tố quyết định mức độ tuân thủ của FL với ngôn ngữ của lĩnh vực chủ đề;
5) sự không chắc chắn của tiêu chí so sánh hình ảnh tìm kiếm (tính đầy đủ của các biện pháp đo khoảng cách chính thức được triển khai trong AIPS cụ thể);
6) sự không chắc chắn trong việc giải thích POS (tính chủ quan và không đầy đủ trong việc tái cấu trúc ý nghĩa của các tài liệu được tìm thấy của người dùng).

---

Не являясь практически измеримыми величинами, эти параметры тем не менее позволяют обозначить характер изменения состояния сторон и структурировать про-цесс, выделяя компоненты не столько по функциональному, сколько по структурному принципу. Причем, первые четыре вида неопределенности имеют информационную природу (преобразование форм представления информации), пятая характеризует по-исковый аппарат АИПС, а шестая отражает когнитивные особенности человека – при-емника и генератора информации.

Mặc dù số lượng không thể đo lường được trên thực tế, nhưng các thông số này vẫn có thể chỉ ra bản chất của sự thay đổi trạng thái của các bên và cấu trúc quy trình, làm nổi bật các thành phần không quá theo chức năng cũng như theo nguyên tắc cấu trúc. Hơn nữa, bốn loại không chắc chắn đầu tiên có tính chất thông tin (chuyển đổi hình thức trình bày thông tin), loại thứ năm đặc trưng cho bộ máy tìm kiếm của AIPS và loại thứ sáu phản ánh đặc điểm nhận thức của một người - người nhận và tạo thông tin.

### 6.2.3. Формы выражения запроса

В вопросно-ответной логике обнаружения нового знания [Белнап, 1981] одной из основных форм вопроса является форма в виде списка альтернатив ответа и правил (алгоритмов) построения прямого ответа на основе этого списка. В этом контексте ин-формационный поиск средствами неинтеллектуальной3 АИПС может рассматриваться как процесс нахождения сообщений, предположительно содержащих прямой ответ, причем не обязательно полный и точный.

Trong logic hỏi đáp khám phá kiến ​​thức mới [Belnap, 1981], một trong những dạng chính của câu hỏi là dạng danh sách các phương án trả lời và các quy tắc (thuật toán) để xây dựng câu trả lời trực tiếp dựa trên danh sách này. . Trong bối cảnh này, tìm kiếm thông tin bằng AIPS phi trí tuệ3 có thể được coi là một quá trình tìm kiếm các tin nhắn được cho là chứa câu trả lời trực tiếp và không nhất thiết phải là câu trả lời đầy đủ và chính xác.

---

Эта особенностью поисковой ситуации, а также то, что пользователь за новым знанием обращается в массив уже известного знания (хотя, возможно, и противоречи-вого4), предопределяет очевидность того, что наиболее адекватной формой представле-ния запроса является гипотетический документ, описывающий реальный, создавае-мый или предполагаемый объект. То есть, в этом контексте задача поиска может быть сформулирована следующим образом: найти уже существующие документы, кото-рые являются содержательным аналогом запрашиваемого гипотетического5.

Đặc điểm này của tình huống tìm kiếm, cũng như thực tế là người sử dụng kiến ​​thức mới chuyển sang một mảng kiến ​​thức đã biết (mặc dù có thể mâu thuẫn4), cho thấy rõ rằng hình thức trình bày yêu cầu thích hợp nhất là một tài liệu giả định mô tả một một đối tượng thực sự được tạo ra hoặc dự định. Nghĩa là, trong bối cảnh này, nhiệm vụ tìm kiếm có thể được xây dựng như sau: tìm các tài liệu đã có sẵn tương tự có ý nghĩa với giả thuyết được yêu cầu5.

---

В рамках свойственной АИПС атрибутивной модели представления смысла (в том числе и вопроса) объект задается набором характеристических признаков и связей. В этом контексте запрос, рассматриваемый на понятийном уровне, может быть пред-ставлен как структурно-логическое определение неизвестного через известные харак-теристические признаки и связи самого объекта, если этот предполагаемый объект су-ществует (реально или гипотетически), или, в противном случае – через дополнение, т. е. характеристические признаки и связи объектов, с которыми связан искомый объект или частью которых он является.

Trong khuôn khổ mô hình thuộc tính đặc trưng biểu đạt ý nghĩa của AIPS (bao gồm cả câu hỏi), một đối tượng được xác định bởi một tập hợp các đặc điểm và mối liên hệ đặc trưng. Trong bối cảnh này, một yêu cầu, được xem xét ở cấp độ khái niệm, có thể được trình bày dưới dạng định nghĩa logic-cấu trúc của điều chưa biết thông qua các đặc điểm đã biết và các kết nối của chính đối tượng đó, nếu đối tượng được cho là này tồn tại (thực tế hoặc giả thuyết), hoặc, nếu không thì - thông qua sự bổ sung, tức là các đặc điểm và mối liên hệ đặc trưng của các đối tượng mà đối tượng mong muốn được liên kết hoặc là một phần của đối tượng đó.

---

Для человека идеальной коммуникативной формой представления реальной ИП является вербальная, где характеристические признаки неизвестного (искомого) будут связаны с конкретным контекстом проблемной ситуации, т. е. запрос фактически будет представлен как документ, содержащий высказывания, которые в гипотетической фор-ме описывают предположительно существующие объекты.

Đối với một người, hình thức giao tiếp lý tưởng để đại diện cho IP thực là bằng lời nói, trong đó các đặc điểm đặc trưng của điều chưa biết (được tìm kiếm) sẽ được liên kết với bối cảnh cụ thể của tình huống có vấn đề, tức là yêu cầu sẽ thực sự được trình bày dưới dạng tài liệu chứa các tuyên bố ở dạng giả thuyết mô tả các đối tượng được cho là hiện có.

---

Принципиально важной особенностью вербального способа является изначаль-ная контекстная определенность (хотя этот контекст, возможно, представлен только в сознании высказывающего). Т. е. отдельное высказывание, воспринимаемое как грам-матическая форма (предложение), в общем случае может порождать в сознании вос-принимающего несколько смыслов, а исходный смысл высказывания будет воспринят только при условии одновременной передачи исходного контекста.

Một đặc điểm quan trọng cơ bản của phương pháp ngôn từ là sự chắc chắn ban đầu về ngữ cảnh (mặc dù ngữ cảnh này có thể chỉ được thể hiện trong tâm trí người nói). Nghĩa là, một phát biểu riêng biệt, được coi là một hình thức ngữ pháp (câu), trong trường hợp tổng quát có thể tạo ra nhiều nghĩa trong tâm trí người nhận thức, và ý nghĩa ban đầu của phát biểu sẽ chỉ được cảm nhận nếu bối cảnh ban đầu được truyền tải đồng thời.

---

Отметим, что именно это явное или неявное использование при восприятии си-туационной или собственной контекстной составляющей позволяет человеку извлекать из текста больше информации, чем явно выражено словами. Соответственно, смысл слов на основе этого контекста может быть развернут до полных высказываний. Такое развертывание при восприятии текста человеком происходит неосознанно: человек, восстанавливая или генерируя смысл, не производит явного выделения лингвистиче-ских, логических и предметных компонентов в полученном сообщении – в сознании человека они неотделимы друг от друга и не представлены в «чистом» виде.

Chúng ta hãy lưu ý rằng chính cách sử dụng rõ ràng hoặc ngầm định này khi nhận thức một thành phần ngữ cảnh hoặc tình huống của chính mình cho phép một người trích xuất nhiều thông tin từ văn bản hơn những thông tin được thể hiện rõ ràng bằng lời. Theo đó, nghĩa của từ dựa trên ngữ cảnh này có thể được mở rộng thành các câu hoàn chỉnh. Sự diễn ra như vậy khi một người nhận thức một văn bản xảy ra một cách vô thức: một người, khôi phục hoặc tạo ra ý nghĩa, không phân biệt rõ ràng các thành phần ngôn ngữ, logic và nội dung trong thông điệp nhận được - trong tâm trí con người, chúng không thể tách rời nhau và không được trình bày theo một cách dạng “tinh khiết”.

---

Запрос с точки зрения способа его представления – это так же, как и в случае до-кумента, терминологическое выражение, представляющее гипотетический объект через описание свойств (атрибутов, связей), наличие которых как признаков (зачастую уже безотносительно характера атрибутов и связей) должна проверить ИС в документах БД. Причем, для машинной формы запроса (ПОЗ) характерно то, что вопросы типа «Как?» и «Почему?» в итоге должны быть преобразованы в вопрос типа «Так ли?» и «Потому ли?», поскольку именно такая форма представления потребности является наиболее адекватной теоретико-множественой модели поиска «на наличие» признака. Суще-ственно, что такое преобразование вопроса в запрос имеет принципиально качествен-ный характер.

Một truy vấn từ quan điểm về phương pháp trình bày của nó, giống như trong trường hợp một tài liệu, là một biểu thức thuật ngữ thể hiện một đối tượng giả định thông qua mô tả các thuộc tính (thuộc tính, kết nối), sự hiện diện của chúng dưới dạng dấu hiệu (thường là bất kể bản chất của các thuộc tính và kết nối) phải được kiểm tra IS trong các tài liệu cơ sở dữ liệu. Hơn nữa, đặc điểm của biểu mẫu yêu cầu máy (PRF) là những câu hỏi như “Làm thế nào?” và "Tại sao?" cuối cùng nên được chuyển thành một câu hỏi như “Có phải vậy không?” và “Đó có phải là lý do không?”, vì chính hình thức thể hiện nhu cầu này là phù hợp nhất với mô hình lý thuyết tập hợp nhằm tìm kiếm “sự hiện diện” của một đặc điểm. Điều quan trọng là việc chuyển đổi một câu hỏi thành một yêu cầu về cơ bản phải có tính chất định tính.

---

Вербальная форма запроса – это терминологическое выражение, с помощью синтаксиса ИПЯ отражающее свойства и связи объектов ПрО. Ей свойственно то, что она предполагает построение завершенного, логически и синтаксически правильного выражения. Такой подход «по духу» отражает стремление к точности выражения, ис-ключающей возможность многозначности ответа, и, соответственно, в минимальной степени учитывает свойство комбинативности. По существу это отражает целеустрем-ленность субъекта поиска, уверенно и априори предполагающего определенность вы-бора, в противоположность неуверенности, предполагающей уместность, в том числе, случайного или эвристического пути получения эффективного решения. В условиях, когда семантическая неопределенность отсутствует, вербальная форма, безусловно, предпочтительнее, как предпочтительнее аналитический способ задания математиче-ской функции по сравнению, например, с табличным.

Hình thức bằng lời của một yêu cầu là một biểu thức thuật ngữ, sử dụng cú pháp của IPL, phản ánh các thuộc tính và kết nối của các đối tượng SbA. Nó được đặc trưng bởi thực tế là nó liên quan đến việc xây dựng một biểu thức hoàn chỉnh, chính xác về mặt logic và cú pháp. Cách tiếp cận “về tinh thần” này phản ánh mong muốn về độ chính xác của cách diễn đạt, loại trừ khả năng mơ hồ trong câu trả lời, và theo đó, tính chất kết hợp được tính đến ở mức độ tối thiểu. Về cơ bản, điều này phản ánh mục đích của chủ thể tìm kiếm, người tự tin và tiên nghiệm thừa nhận sự chắc chắn của sự lựa chọn, trái ngược với sự không chắc chắn, vốn giả định sự phù hợp của, trong số những thứ khác, một cách ngẫu nhiên hoặc theo kinh nghiệm để có được một giải pháp hiệu quả. Trong những điều kiện không có sự không chắc chắn về mặt ngữ nghĩa, hình thức bằng lời nói chắc chắn được ưu tiên hơn, cũng như phương pháp phân tích để xác định hàm toán học được ưu tiên hơn so với phương pháp dạng bảng chẳng hạn.

---

Такая форма для случая атрибутивного поиска практически полностью вопло-щена в технологиях SQL для реляционных БД – языке манипулирования данными для предопределенной семантики этих данных. Для тематического поиска, когда, по край-ней мере, один из атрибутов полностью не специфицирован, использование вербальной формы потребует в общем случае формулирования такого числа выражений, сколько значений может иметь этот атрибут. В этом случае, исходя из принципа «наименьшего действия», вариантом решения может быть формирование в ответ на запрос, представ-ленный терминологическим выражением, ряда кластеров документов, соответствую-щих различным комбинациям терминов.

Hình thức này dành cho trường hợp tìm kiếm thuộc tính gần như được thể hiện hoàn toàn trong các công nghệ SQL dành cho cơ sở dữ liệu quan hệ - một ngôn ngữ thao tác dữ liệu dành cho ngữ nghĩa được xác định trước của dữ liệu này. Đối với tìm kiếm theo chủ đề, khi ít nhất một trong các thuộc tính không được chỉ định đầy đủ, việc sử dụng dạng động từ thường sẽ yêu cầu xây dựng nhiều biểu thức bằng số lượng giá trị mà thuộc tính đó có thể có. Trong trường hợp này, dựa trên nguyên tắc “ít hành động nhất”, một giải pháp có thể là hình thành, để đáp ứng yêu cầu được biểu thị bằng một biểu thức thuật ngữ, một số cụm tài liệu tương ứng với các tổ hợp thuật ngữ khác nhau.

---

С другой стороны, содержание потребности частично или полностью может быть представлено реально существующими в БД документами (как сообщениями, со-держащими решения проблемной ситуации или имеющими какую-либо семантическую общность с ИП). В этом случае можно говорить о кластерной форме, сводящей поня-тие «документ» или «совокупность документов» к понятию запроса.

Mặt khác, nội dung của nhu cầu có thể được thể hiện một phần hoặc toàn bộ bằng các tài liệu thực sự tồn tại trong cơ sở dữ liệu (dưới dạng các thông điệp chứa giải pháp cho một tình huống có vấn đề hoặc có một số điểm tương đồng về ngữ nghĩa với cá nhân doanh nhân). Trong trường hợp này, chúng ta có thể nói về một dạng cụm, làm giảm khái niệm “tài liệu” hoặc “bộ tài liệu” thành khái niệm yêu cầu.

---

Эти формы являются альтернативными, но скорее взаимодополняющими, чем взаимно исключающими, что воплотилось в практике АИПС в виде двух уже привыч-ных форм поискового запроса в диалоге «человек-система» – запросно-ответной и ги-пертекстовой.

Các hình thức này là thay thế, nhưng bổ sung hơn là loại trừ lẫn nhau, được thể hiện trong thực tiễn AIPS dưới dạng hai dạng truy vấn tìm kiếm quen thuộc trong cuộc đối thoại “hệ thống con người” – truy vấn-phản hồi và siêu văn bản.

---

С точки зрения свойства комбинативности, как основы любого ИПЯ, и запрос, и документ являются моделями, представляющими средствами языка отдельные части и аспекты некоторого целостного фрагмента предметной области. Документ является конкретной (хотя и не единственной) формой выражения определенной проблемной ситуации (разрешение которой было предметом ОД, приведшей к появлению этого до-кумента). ПОД представляет конкретику содержания документа композицией в общем случае не уникальных характеристических признаков, выбираемых из множества при-знаков, свойственных и другим объектам, информация о которых хранится в БД.

Từ quan điểm về tính chất kết hợp, với tư cách là nền tảng của bất kỳ ngoại ngữ nào, cả yêu cầu và tài liệu đều là các mô hình thể hiện các bộ phận và khía cạnh riêng lẻ của một số phần không thể thiếu của lĩnh vực chủ đề bằng ngôn ngữ. Tài liệu là một hình thức thể hiện cụ thể (mặc dù không phải là duy nhất) của một tình huống vấn đề nhất định (việc giải quyết vấn đề đó là chủ đề của OA dẫn đến sự xuất hiện của tài liệu này). POD thể hiện các chi tiết cụ thể của nội dung tài liệu bằng cách tổng hợp các đặc điểm chung không duy nhất được chọn từ nhiều đặc điểm khác nhau đặc trưng của các đối tượng khác, thông tin về chúng được lưu trữ trong cơ sở dữ liệu.

---

Цель создания ПОД – представить изначально уникальный смысл документа компактной композицией признаков (например, в случае дескрипторных ИПЯ - ключе-выми словами), по возможности, не увеличивая комбинативность порождаемых ими возможных смыслов. Цель построения ПОЗ – сохраняя уникальность проблемной си-туации, увеличить комбинативность смыслов, порождаемых композицией поисковых признаков запроса, для того, чтобы максимально охватить аспекты представления объ-екта поиска.

Mục đích của việc tạo PML là trình bày ý nghĩa duy nhất ban đầu của một tài liệu với thành phần nhỏ gọn của các tính năng (ví dụ: trong trường hợp bộ mô tả IPL - từ khóa), nếu có thể, mà không làm tăng khả năng kết hợp các ý nghĩa có thể do chúng tạo ra . Mục đích của việc xây dựng POS là để duy trì tính duy nhất của tình huống vấn đề và tăng khả năng kết hợp các ý nghĩa được tạo ra bởi sự kết hợp của các tính năng truy vấn tìm kiếm nhằm bao quát tối đa các khía cạnh của việc trình bày đối tượng tìm kiếm.

---

В табл. 6.2 приведены возможные способы представления (выражения) инфор-мационных потребностей для разных типов поисковых задач (видов поиска).

Trong bảng 6.2 chỉ ra các cách thể hiện (thể hiện) nhu cầu thông tin cho các loại nhiệm vụ tìm kiếm khác nhau (các loại tìm kiếm).

---

Таблица 6.2. Выражение информационных потребностей для разных видов поиска

| Вид поиска | Характер ИП | Известное/неизвестное в предмете поиска | Состав ПОЗ |
| --- | --- | --- | --- |
| Предметный (атрибутив-ный) поиск | Найти документы, содержа-щие информацию об извест-ном объекте (факте) по из-вестным значениям характе-ристических признаков | Объект полностью опреде-лен признаками и/или свя-зями. \\ Неизвестно значение от-дельного признака или свя-зи | Термины индексирова-ния документов, отне-сенные к семантически определенным полям |
| Тематический поиск | Найти документы, содержа-щие информацию о гипоте-тическом объекте (или мето-де его построения) по пред-полагаемым характеристиче-ским или ассоциированным признакам и связям |Объект задан частью при-знаков/связей; полностью известна структура, как си-стемное свойство, опреде-ляющее целостность. \\ Неизвестны отдельные при-знаки или связи | Термины документов и термины дополнитель-ных поисковых струк-тур – тематических рубрикаторов, тезауру-сов и т. п., отнесенные к семантически опреде-ленным полям |
| Проблемный поиск | Найти документы, позволя-ющие определить информа-ционное пространство, под-тверждающее/отрицающее возможность постановки и решения задачи; поиск ново-го качества в предметной области | Объект задан частью при-знаков/связей; структура, как системное свойство, определяющее целостность, полностью не определена. \\ Неизвестны отдельные группы признаки/связи или структура | Документы, входящие в итеративно формируе-мое пользователем ин-формационное про-странство |

---

Вышеизложенное является основанием для утверждения, что форма и способ представления запроса принципиально имеет двойственную природу: при стремлении к «завершённой» вербальной (однородной и целостной) форме выражения запроса в силу неизвестности, присущей реальной ИП (и потому невозможности построения адекват-ного выражения в вербальной форме), часть или весь запрос может быть представлен в форме отдельных документов или их кластеров, что соответствует дискретной, «моза-ичной» кластерной форме. При этом свойство комбинативности используется для по-следовательного снятия множественной неопределенности за счет введения процедур-ной избыточности – механизмов порождения и упорядочения кластеров документов. Определение корреляционных связей между кластерами внутри отдельной выдачи и кластерами различных выдач позволяют определить относительные (пусть только внут-ри контекстного поля – множества документов, имеющих отношение к выраженной информационной потребности) полноту и точность, а также оценить сходимость про-цесса поиска.

Trên đây là cơ sở để khẳng định hình thức và phương pháp trình bày yêu cầu về cơ bản có tính chất kép: khi phấn đấu đạt được một hình thức thể hiện yêu cầu bằng lời nói “hoàn chỉnh” (đồng nhất và toàn diện) do cái chưa biết vốn có trong thực tế. IP (và do đó không thể xây dựng một biểu thức đầy đủ ở dạng bằng lời nói), một phần hoặc toàn bộ yêu cầu có thể được trình bày dưới dạng các tài liệu riêng lẻ hoặc các cụm của chúng, tương ứng với một dạng cụm “khảm” rời rạc. Trong trường hợp này, tính chất kết hợp được sử dụng để loại bỏ một cách nhất quán nhiều điểm không chắc chắn thông qua việc đưa ra tính dư thừa thủ tục - cơ chế tạo và sắp xếp các cụm tài liệu. Việc xác định mối tương quan giữa các cụm trong một kết quả tìm kiếm duy nhất và các cụm kết quả tìm kiếm khác nhau cho phép chúng tôi xác định mối tương quan (ngay cả khi chỉ trong trường ngữ cảnh - một tập hợp các tài liệu liên quan đến nhu cầu thông tin được thể hiện) tính đầy đủ và chính xác, cũng như để đánh giá sự hội tụ của quá trình tìm kiếm.

## 6.3. Компоненты и обобщенная схема информационного поиска

Особенности представления информации в документальных БД определяются их назначением – обеспечением эффективного (быстрого и исчерпывающего, прежде всего, по полноте) поиска нужных данных или, если таковые не обнаружены, – сведений о документах, предположительно их содержащих. Каждому типу поиска соответствует свой тип запроса, форма его выражения и, соответственно, характер результата. В первом случае необходимо найти все о некотором объекте – в результате пользователь получает некоторую выдачу, где нужные сведения присутствуют в явном виде. При решении задач, требующих использования поиска второго типа, строится предметная область проблемы, описываются объекты и связи и затем осуществляется поиск недостающих объектов и/или связей. В результате пользователь получает выдачу, где присутствует (или нет) понятие, которое может быть использовано для построения нового объекта, а не только для подтверждения факта его существования. Задачи, которые решаются с помощью поиска третьего типа, характеризуются тем, что тема запроса зачастую формируется или изменяется непосредственно в процессе поиска.

Các tính năng của việc trình bày thông tin trong cơ sở dữ liệu tài liệu được xác định bởi mục đích của chúng - cung cấp khả năng tìm kiếm hiệu quả (nhanh chóng và toàn diện, chủ yếu về tính đầy đủ) cho dữ liệu cần thiết hoặc, nếu không tìm thấy, thông tin về các tài liệu được cho là có chứa chúng. Mỗi loại tìm kiếm tương ứng với loại yêu cầu riêng, hình thức biểu hiện của nó và theo đó, bản chất của kết quả. Trong trường hợp đầu tiên, cần phải tìm mọi thứ về một đối tượng nhất định - kết quả là người dùng nhận được một số đầu ra, trong đó thông tin cần thiết được trình bày ở dạng rõ ràng. Khi giải quyết các vấn đề yêu cầu sử dụng loại tìm kiếm thứ hai, miền vấn đề được xây dựng, các đối tượng và kết nối được mô tả, sau đó tìm kiếm các đối tượng và/hoặc kết nối bị thiếu. Kết quả là, người dùng nhận được kết quả trong đó có (hoặc không có) một khái niệm có thể được sử dụng để xây dựng một đối tượng mới chứ không chỉ để xác nhận thực tế về sự tồn tại của nó. Các vấn đề được giải quyết bằng loại tìm kiếm thứ ba có đặc điểm là chủ đề của truy vấn thường được hình thành hoặc thay đổi trực tiếp trong quá trình tìm kiếm.

---

Семантическая тривиальность структур данных, реализующих документальные системы в фон-Неймановской архитектуре вычислительных машин, предопределяет, что развитие запроса и смысловая оценка результата поиска – исключительно прерога-тива пользователя, а не системы. И даже принимая во внимание определенные успехи в области разработок искусственного интеллекта, по крайней мере, два следующих фак-тора не позволяют надеяться на скорое равноправие сторон:

- выражение запроса на естественном языке (даже хорошо формализованное) слиш-ком лаконично для того, чтобы можно было бы выделить глубинную сущность про-блемы, для решения которой должна быть найдена информация;
- в ряде случаев пользователь не может однозначно специфицировать (выразить наличными лингвистическими и понятийными средствами) информационную по-требность, особенно если она связана с этапом постановки задачи.

Tính tầm thường về ngữ nghĩa của các cấu trúc dữ liệu triển khai các hệ thống tài liệu trong kiến ​​trúc von Neumann của máy tính xác định trước rằng việc phát triển truy vấn và đánh giá ngữ nghĩa của kết quả tìm kiếm chỉ là đặc quyền của người dùng chứ không phải của hệ thống. Và ngay cả khi tính đến những thành công nhất định trong lĩnh vực phát triển trí tuệ nhân tạo, ít nhất hai yếu tố sau không cho phép chúng ta hy vọng vào sự bình đẳng nhanh chóng giữa các bên:

- cách diễn đạt yêu cầu bằng ngôn ngữ tự nhiên (ngay cả khi được chính thức hóa tốt) quá ngắn gọn để có thể làm nổi bật bản chất sâu xa của vấn đề cần tìm thông tin;
- trong một số trường hợp, người dùng không thể xác định rõ ràng (thể hiện bằng các phương tiện ngôn ngữ và khái niệm sẵn có) một nhu cầu thông tin, đặc biệt nếu nó liên quan đến giai đoạn hình thành vấn đề.

---

Как отмечалось ранее, система является лишь инструментом, используемым человеком при поиске информации, поэтому эффективность ее использования зависит от того, насколько хорошо сам человек – получатель и потребитель информации, знает природу и свойства объектов и инструментов, с которыми он работает.

Như đã lưu ý trước đó, hệ thống chỉ là một công cụ được một người sử dụng khi tìm kiếm thông tin, do đó hiệu quả của việc sử dụng nó phụ thuộc vào mức độ hiểu biết của bản thân người đó, người nhận và người tiêu dùng thông tin, về bản chất và tính chất của đối tượng và công cụ. mà anh ấy làm việc cùng.

### 6.3.1. Основные понятия и определения поисковых компонентов ИС

Функционирование современных ИПС основывается на двух предположениях:

1) документы, необходимые пользователю, объединены наличием некоторого характе-ристического признака или комбинации признаков;
2) пользователь способен указать эти признаки. Оба эти предположения на практике редко выполняются и можно гово-рить только о вероятности их выполнения. Поэтому, процесс поиска информации обычно представляет собой последовательность шагов, приводящих при посредстве си-стемы к результату, качество которого будет иметь случайную природу и определяться многими факторами. При этом поведение пользователя, как организующее начало управления процессом поиска, определяется не только информационной потребностью, но и инструментальным разнообразием системы – технологиями и средствами, предо-ставляемыми системой.

Hoạt động của các hệ thống thông tin hiện đại dựa trên hai giả định:

1) các tài liệu mà người dùng yêu cầu được thống nhất bởi sự hiện diện của một số tính năng đặc trưng hoặc sự kết hợp của các tính năng;
2) người dùng có thể chỉ ra những đặc điểm này. Cả hai giả định này hiếm khi được đáp ứng trong thực tế và chúng ta chỉ có thể nói về xác suất thực hiện của chúng. Do đó, quá trình tìm kiếm thông tin thường thể hiện một chuỗi các bước dẫn đến kết quả thông qua hệ thống, chất lượng của kết quả đó sẽ mang tính chất ngẫu nhiên và được xác định bởi nhiều yếu tố. Đồng thời, hành vi của người dùng, với tư cách là khởi đầu của tổ chức quản lý quá trình tìm kiếm, không chỉ được xác định bởi nhu cầu thông tin mà còn bởi sự đa dạng về công cụ của hệ thống - các công nghệ và công cụ do hệ thống cung cấp.

---

Для единообразного понимания и использования определим «в комплексе» эти важные с точки зрения моделирования и эксплуатации ИПС понятия, содержание кото-рых подробно будет рассматриваться далее.

Để hiểu và sử dụng thống nhất, chúng tôi sẽ định nghĩa “một cách phức tạp” những khái niệm quan trọng này theo quan điểm mô hình hóa và vận hành hệ thống thông tin, nội dung của chúng sẽ được thảo luận chi tiết bên dưới.

---

Методы поиска – это совокупность моделей и алгоритмов реализации отдель-ных технологических этапов, таких, как построение поискового образа запроса, отбор документов (сопоставление поисковых образов запросов и документов), расширение и реформулирование запроса, локализация и оценка выдачи.

Phương pháp tìm kiếm là tập hợp các mô hình và thuật toán để thực hiện các giai đoạn công nghệ riêng lẻ, chẳng hạn như xây dựng hình ảnh tìm kiếm của truy vấn, chọn tài liệu (so sánh hình ảnh tìm kiếm của truy vấn và tài liệu), mở rộng và định dạng lại truy vấn, bản địa hóa và đánh giá kết quả tìm kiếm.

---

Механизмами поиска будем называть реализованные в конкретной АИПС моде-ли и алгоритмы процесса формирования выдачи документов в ответ на поисковый за-прос.

Cơ chế tìm kiếm sẽ là các mô hình và thuật toán của quá trình tạo đầu ra tài liệu được triển khai trong AIPS cụ thể để đáp ứng truy vấn tìm kiếm.

---

Средства поиска – это комплекс ИПЯ и языков определения/управления дан-ными, обеспечивающих представление и структурно-семантические преобразования основных и технологических объектов (документов, словарей, совокупностей результа-тов поиска), а также средства управления, обеспечивающие с помощью пользователь-ского интерфейса доступ к операционным объектам и функциям конкретной АИПС.

Các công cụ tìm kiếm là một tổ hợp các ngôn ngữ nước ngoài và ngôn ngữ quản lý/định nghĩa dữ liệu cung cấp cách trình bày và chuyển đổi ngữ nghĩa cấu trúc của các đối tượng cơ bản và công nghệ (tài liệu, từ điển, bộ kết quả tìm kiếm), cũng như các công cụ quản lý cung cấp, sử dụng giao diện người dùng để truy cập vào các phương tiện và chức năng hoạt động của một AIPS cụ thể.

---

Поисковые технологии – унифицированные (и оптимизированные в рамках кон-кретной АИПС) последовательности использования в процессе взаимодействия пользо-вателя с системой отдельных средств поиска для устойчивого и эффективного получе-ния конечного и промежуточных результатов.

Các công nghệ tìm kiếm được thống nhất (và được tối ưu hóa trong khuôn khổ AIPS cụ thể) theo trình tự sử dụng trong quá trình tương tác của người dùng với hệ thống các công cụ tìm kiếm riêng lẻ để thu được kết quả cuối cùng và trung gian một cách bền vững và hiệu quả.

---

Стратегия поиска – общий план (концепция, предпочтение, предрасположен-ность, установка) поведения пользователя для выражения и удовлетворения информа-ционной потребности, обусловленный как характером цели и типом поиска, так и си-стемными «стратегическими» решениями – архитектурой БД, а также методами и сред-ствами поиска конкретной АИПС. Выбор стратегии в общем случае является оптими-зационной задачей, однако на практике в значительной степени определяется искус-ством достижения компромисса между практическими потребностями и возможностя-ми имеющихся средств. С точки зрения способа задания условия соответствия инфор-мационной потребности информационным ресурсам можно говорить о двух «чистых» стратегиях – «вербальной», являющейся аналогом функционального задания, и «кла-стерной», отражающей особенности перечислительного способа.

Chiến lược tìm kiếm là một kế hoạch chung (khái niệm, sở thích, khuynh hướng, thái độ) về hành vi của người dùng nhằm thể hiện và đáp ứng nhu cầu thông tin, được xác định bởi cả bản chất của mục tiêu và loại hình tìm kiếm cũng như bởi các quyết định “chiến lược” mang tính hệ thống - kiến ​​trúc cơ sở dữ liệu, cũng như cũng như các phương pháp và phương tiện tìm kiếm một AIPS cụ thể. Việc lựa chọn chiến lược trong trường hợp chung là một vấn đề tối ưu hóa, nhưng trên thực tế, nó phần lớn được quyết định bởi nghệ thuật đạt được sự thỏa hiệp giữa nhu cầu thực tế và khả năng của các phương tiện sẵn có. Từ quan điểm của phương pháp thiết lập điều kiện cho sự tương ứng của nhu cầu thông tin với tài nguyên thông tin, chúng ta có thể nói về hai chiến lược “thuần túy” – “bằng lời nói”, tương tự như một nhiệm vụ chức năng và “cụm”, phản ánh đặc điểm của phương pháp đếm.

---

Навигация как реализация процесса поиска по запросу в выбранной БД - это це-ленаправленная, определяемая стратегией последовательность использования методов, средств и технологий конкретной АИПС для получения и оценки результата.

Điều hướng là việc triển khai quy trình tìm kiếm truy vấn trong cơ sở dữ liệu đã chọn là một trình tự có mục đích, được xác định theo chiến lược sử dụng các phương pháp, công cụ và công nghệ của một AIPS cụ thể để thu được và đánh giá kết quả.

---

Средства навигации позволяют пользователю осуществлять управление процес-сом поиска. Такие средства предоставляются пользователю в виде интерфейса, позво-ляющего организовать более или менее эффективный процесс взаимодействия с БД.

Công cụ điều hướng cho phép người dùng kiểm soát quá trình tìm kiếm. Các công cụ như vậy được cung cấp cho người dùng dưới dạng giao diện cho phép tổ chức một quá trình tương tác ít nhiều hiệu quả với cơ sở dữ liệu.

### 6.3.2. Обобщенная схема информационного поиска

Процесс поиска информации представляет собой последовательность шагов, приводящих при посредстве системы к некоторому результату и позволяющих оценить его полноту (может ли пользователь быть уверенным в том, что полученный результат – исчерпывающий и ничего более по искомой проблеме не содержит). Так как пользователь обычно не имеет исчерпывающих знаний об информационном содержании ресурса, в котором проводит поиск, то оценить адекватность выражения запроса, равно как и полноту получаемого результата, он может, основываясь лишь на внешних оценках или на промежуточных результатах и обобщениях, сопоставляя их, например, с предыдущими.

Quá trình tìm kiếm thông tin là một chuỗi các bước mà thông qua hệ thống sẽ dẫn đến một kết quả nhất định và cho phép người ta đánh giá tính đầy đủ của nó (người dùng có thể chắc chắn rằng kết quả thu được là toàn diện và không chứa thêm bất kỳ điều gì về vấn đề không? đang được tìm kiếm). Vì người dùng thường không có kiến ​​​​thức toàn diện về nội dung thông tin của tài nguyên mà anh ta đang tìm kiếm, nên anh ta có thể đánh giá tính đầy đủ của biểu thức truy vấn, cũng như tính đầy đủ của kết quả thu được, chỉ dựa trên các đánh giá bên ngoài hoặc dựa trên các đánh giá trung gian. kết quả và khái quát hóa, ví dụ, so sánh chúng với những kết quả trước đó.

---

В контексте рис. 6.2 задача поискового процесса – построить согласованную си-стему моделей объекта поиска. То есть для осознанной, зафиксированной в сознании человека информационной потребности сформировать множество лингвистических об-разов в среде АИПС. Для информационной цепи формирования ПОЗ – это две имею-щие лингвистическую природу модели, относящиеся к двум верхним уровням:

1) мо-дель коммуникативная, являющаяся представлением ИП, ориентированным на переда-чу для соотнесения с аналогично представленными объектами, описанными в уже опубликованных документах;
2) модель поисковая, атрибутивно6 представляющая ИП и ориентированная на точечное (теоретико-множественное) соотнесение с аналогично представленными поисковыми образами документов.

Trong bối cảnh của Hình. 6.2 Nhiệm vụ của quá trình tìm kiếm là xây dựng một hệ thống nhất quán các mô hình của đối tượng tìm kiếm. Nghĩa là, đối với nhu cầu thông tin có ý thức, được ghi lại trong tâm trí con người, hình thành nên nhiều hình ảnh ngôn ngữ khác nhau trong môi trường AIPS. Đối với chuỗi thông tin hình thành, POS là hai mô hình mang tính chất ngôn ngữ, thuộc hai cấp độ trên:

1) một mô hình giao tiếp, là sự thể hiện của IP, tập trung vào việc truyền tải để tương quan với các đối tượng được thể hiện tương tự được mô tả trong các tài liệu đã được xuất bản;
2) một mô hình tìm kiếm, theo cách phân bổ6 đại diện cho IP và tập trung vào mối tương quan từng điểm (lý thuyết tập hợp) với các hình ảnh tìm kiếm được trình bày tương tự của các tài liệu.

---

Согласованность здесь имеет двоякий смысл: очевидное (вертикальное) соответ-ствие выражения поисковому образу документа (ПОД – это выражение содержания до-кумента, представленное средствами ИПЯ), и «горизонтальное» соответствие пред-ставления пользователя реальным возможностям языка для выражения ИП.

Tính nhất quán ở đây có hai nghĩa: sự tương ứng rõ ràng (theo chiều dọc) của biểu thức với hình ảnh tìm kiếm của tài liệu (POD là sự thể hiện nội dung của tài liệu, được biểu thị bằng ngôn ngữ IP) và sự tương ứng “ngang” sự thể hiện của người dùng đối với khả năng thực sự của ngôn ngữ trong việc thể hiện IP.

---

Для того чтобы пользователь имел возможность реально управлять процессом поиска (на основе объективных данных, позволяющих оценить эффективность выполняемых действий), необходимо произвести декомпозицию целостной с точки зрения конечной задачи пользователя запросно-ответной схемы процесса поиска, обобщенная схема которого была рассмотрена во второй главе (см. рис 2.10). Такая функциональная декомпозиция должна в итоге обеспечить возможности для последовательного снятия неопределенностей всех типов, что в организационном плане выражается в выделении подпроцессов-процедур и соответствующих операционных объектов.

Để người dùng có thể thực sự quản lý quá trình tìm kiếm (dựa trên dữ liệu khách quan cho phép người dùng đánh giá hiệu quả của các hành động được thực hiện), cần phải phân tách sơ đồ yêu cầu-phản hồi của quy trình tìm kiếm, mang tính tổng thể. từ quan điểm về nhiệm vụ cuối cùng của người dùng, sơ đồ tổng quát đã được thảo luận trong chương thứ hai (xem .fig 2.10). Sự phân rã chức năng như vậy cuối cùng sẽ tạo cơ hội cho việc loại bỏ nhất quán các loại sự không chắc chắn, mà theo thuật ngữ tổ chức được thể hiện trong việc xác định các quy trình-thủ tục con và các đối tượng vận hành tương ứng.

---

Отметим, что основные компоненты поиска в равной степени могут быть ис-пользованы на следующих стратах преобразования запроса в результат:

- на страте планирования для определения пользователем стратегии поиска;
- на страте организации поиска как системные решения, воплотившие на ста-дии разработки и адаптации системы особенности поведения предполагае-мых пользователей и характер хранимой информации;
- на страте выполнения (навигация) для проведения реальным пользователем конкретного поиска в рамках выбранной им стратегии средствами АИПС.

Lưu ý rằng các thành phần tìm kiếm chính có thể được sử dụng như nhau trong các tầng sau để chuyển đổi truy vấn thành kết quả:

- về tầng lập kế hoạch để người dùng xác định chiến lược tìm kiếm;
- ở cấp tổ chức tìm kiếm dưới dạng giải pháp hệ thống, ở giai đoạn phát triển và điều chỉnh hệ thống, thể hiện các đặc điểm hành vi của người dùng dự định và bản chất của thông tin được lưu trữ;
- trên tầng thực thi (điều hướng) để người dùng thực tế tiến hành tìm kiếm cụ thể trong khuôn khổ chiến lược đã chọn của mình bằng cách sử dụng AIPS.

---

С точки зрения целевого назначения ИС, т. е. для процесса поиска в целом, имеем всего два типа основных операционных объектов – запрос и документ, которые представляют средствами языка некоторый семантически целостный фрагмент предметной области. Другие операционные объекты – технологические в рамках декомпозированного процесса – это самостоятельные семантически значимые объекты метаинформационного назначения или объекты, производные от основных7. Назначение и природа технологических объектов – дать возможность локализовать и снять или зафиксировать неопределенность отдельного типа.

Từ quan điểm về mục đích dự định của IS, tức là đối với toàn bộ quá trình tìm kiếm, chúng tôi chỉ có hai loại đối tượng hoạt động chính - một yêu cầu và một tài liệu, thể hiện, bằng ngôn ngữ, một ngữ nghĩa nhất định không thể thiếu phần của lĩnh vực chủ đề. Các đối tượng hoạt động khác - công nghệ trong khuôn khổ quá trình phân rã - là các đối tượng độc lập có ý nghĩa về mặt ngữ nghĩa cho các mục đích siêu thông tin hoặc các đối tượng bắt nguồn từ các đối tượng chính7. Mục đích và bản chất của các đối tượng công nghệ là giúp định vị và loại bỏ hoặc ghi lại độ không đảm bảo của một loại cụ thể.

---

Необходимость выделения объектов появляется при частичной или полной ав-томатизации. Декомпозиция цельного процесса поиска-восприятия-использования ин-формации необходима для распределения функций между подсистемами. Именно для перехода от предметного уровня (реальной потребности) к лингвистическому (запросу и его поисковому образу) и далее – к технологическому, необходимо явно выделить еще и логический уровень, где в качестве операндов используются понятия и структу-ры, что и обеспечивает переход к формированию формализованной ИП на уровне имен и лингвистических связей.

Nhu cầu chọn đối tượng xuất hiện với sự tự động hóa một phần hoặc toàn bộ. Việc phân rã quá trình tích hợp tìm kiếm-nhận thức-sử dụng thông tin là cần thiết để phân bổ chức năng giữa các hệ thống con. Đối với quá trình chuyển đổi từ cấp độ chủ đề (nhu cầu thực sự) sang ngôn ngữ (truy vấn và hình ảnh tìm kiếm của nó) và xa hơn nữa đến cấp độ công nghệ, cần làm nổi bật rõ ràng cấp độ logic, trong đó các khái niệm và cấu trúc được sử dụng làm toán hạng, trong đó đảm bảo sự chuyển đổi sang IP chính thức hình thành ở cấp độ tên và kết nối ngôn ngữ.

---

В случае процесса построения запроса с использованием слов естественного языка, которым свойственны синонимия и полисемия, для неискажающего смысл меж-уровневого перехода применяются метаинформационные, внешние по отношению к сообщению конструкции, позволяющие фиксировать (выбирать или указывать) кон-текст словоупотребления.

Trong trường hợp quá trình xây dựng truy vấn sử dụng các từ của ngôn ngữ tự nhiên, được đặc trưng bởi từ đồng nghĩa và đa nghĩa, để chuyển đổi giữa các cấp độ không làm sai lệch ý nghĩa, các cấu trúc siêu thông tin được sử dụng bên ngoài thông báo , cho phép ghi lại (chọn hoặc chỉ ra) ngữ cảnh sử dụng từ.

<!-- 6 Напомним, что поскольку информационный поиск реализуется в машинной среде, в основе которой лежит двоичная логика, то процесс любого отбора должен быть сведен к атрибутивной модели, т. е. от-бору через задание имени и значения характеристического свойства (атрибута). Таким образом, только для случая предметного поиска отбор документов может быть реализован по «одноактной» схеме – опе-рацией проверки, есть ли в базе данных документы, имеющие заданное значение атрибута. -->


Полнота и точность передачи контекста при такой организации процесса зависят от вида запроса: для типовых по отношению к предметной области и потому хорошо представленных метаинформационными средствами они могут быть высокими, а для запросов проблемных – низкими. При этом в процессе явно не передается ни контекст, ни характер неопределенности. Поэтому первым шагом должна быть локализация ре-альной ИП – структурно-логическая декомпозиция ПрО, при которой для возможных аспектов рассмотрения объекта поиска выделяются характеристические понятия и свя-зи.

Tính đầy đủ và chính xác của việc truyền ngữ cảnh với cách tổ chức quy trình như vậy phụ thuộc vào loại yêu cầu: đối với các truy vấn thông thường liên quan đến lĩnh vực chủ đề và do đó được thể hiện tốt bằng các phương tiện siêu thông tin, chúng có thể cao và đối với các truy vấn có vấn đề - thấp. Đồng thời, cả bối cảnh lẫn bản chất của sự không chắc chắn đều không được truyền tải rõ ràng trong quy trình. Do đó, bước đầu tiên phải là bản địa hóa một IP thực - sự phân rã cấu trúc và logic của SbA, trong đó các khái niệm và kết nối đặc trưng được xác định cho các khía cạnh có thể có của việc xem xét đối tượng tìm kiếm.

---

Следующий шаг – переход на лингвистический уровень – это нахождение мно-жества имен понятий и, соответственно, терминов ИПЯ, образующих класс условной эквивалентности для каждого из исходных объектов в заданном аспекте. Другими сло-вами, это формирование возможных вариантов грамматических (по крайней мере, тер-минологических) конструкций, выражающих существо ИП в каждом из возможных ас-пектов рассмотрения. Метаинформационный компонент обеспечивает семантику сло-воупотреблений, характерную для языка и отражающую практику его использования при индексировании. Этот шаг достаточно эффективно автоматизируется8, однако ве-роятностный характер процесса построения классов условной эквивалентности пред-полагает обязательность последующей проверки состоятельности гипотезы – оценки пользователем адекватности терминов по степени их важности в контексте найденных по ним документов.

Bước tiếp theo là chuyển sang cấp độ ngôn ngữ - đây là tìm một tập hợp các tên khái niệm và theo đó, các thuật ngữ TL tạo thành một lớp tương đương có điều kiện cho từng đối tượng ban đầu trong một khía cạnh nhất định. Nói cách khác, đây là sự hình thành các biến thể có thể có của các cấu trúc ngữ pháp (ít nhất là về mặt thuật ngữ) thể hiện bản chất của sở hữu trí tuệ trong từng khía cạnh có thể được xem xét. Thành phần siêu thông tin cung cấp ngữ nghĩa của cách sử dụng từ, đặc điểm của ngôn ngữ và phản ánh thực tiễn sử dụng nó trong quá trình lập chỉ mục. Bước này có thể được tự động hóa khá hiệu quả,8 tuy nhiên, bản chất xác suất của quá trình xây dựng các lớp tương đương có điều kiện giả định trước việc xác minh bắt buộc tiếp theo về tính hợp lệ của giả thuyết - đánh giá của người dùng về tính đầy đủ của các thuật ngữ theo mức độ quan trọng của chúng trong bối cảnh của các tài liệu được tìm thấy trên chúng.

---

Несколько иная ситуация при использовании выдачи – содержания документов, найденных по запросу. Значение термина (как лингвистической переменной), его кон-текст как структурной единицы в рамках более крупных конструкций, таких как пред-ложение или документ, определяется пользователем достаточно точно (хотя и субъек-тивно) и обычно без явного использования метаинформации. Менее полно может быть определен смысл композиционных структурных единиц – предложения и сообщения в целом: в лучшем случае можно точно определить, дает содержание документа исчер-пывающий ответ на практический вопрос или нет, однако невозможно знать, исчерпы-вается ли этим весь смысл сообщения. Тем не менее характер и контекст словоупотреб-лений может быть использован в качестве оценки эффективности запроса с точки зре-ния как семантики словоупотребления, так и семантики предметной области.

Tình hình hơi khác khi sử dụng phát hành - nội dung tài liệu được tìm thấy theo yêu cầu. Ý nghĩa của một thuật ngữ (như một biến ngôn ngữ), ngữ cảnh của nó như một đơn vị cấu trúc trong các cấu trúc lớn hơn như một câu hoặc tài liệu, được người dùng xác định khá chính xác (mặc dù về mặt chủ quan) và thường không sử dụng siêu thông tin rõ ràng. Ý nghĩa của các đơn vị cấu trúc thành phần—các câu và thông điệp nói chung—có thể ít được xác định đầy đủ hơn: tốt nhất, có thể xác định chính xác liệu nội dung của tài liệu có cung cấp câu trả lời toàn diện cho một câu hỏi thực tế hay không, nhưng điều đó là không thể để biết liệu điều này có làm cạn kiệt toàn bộ ý nghĩa của thông điệp hay không. Tuy nhiên, bản chất và bối cảnh sử dụng từ có thể được sử dụng để đánh giá tính hiệu quả của một truy vấn từ quan điểm của cả ngữ nghĩa của việc sử dụng từ và ngữ nghĩa của lĩnh vực chủ đề.

---

Соответственно, использование в запросе терминов, выбираемых из текста реле-вантных документов, является по существу реализацией схемы реформулирования за-проса по обратной связи. По характеру контекста здесь имеется два типа обратной свя-зи: внутренняя – на лингвистическом уровне, и внешняя – на уровне семантики пред-метной области.

Theo đó, việc sử dụng trong truy vấn các thuật ngữ được chọn từ văn bản của các tài liệu liên quan về cơ bản là triển khai sơ đồ cải cách truy vấn dựa trên phản hồi. Theo tính chất của ngữ cảnh, có hai loại phản hồi: phản hồi bên trong - ở cấp độ ngôn ngữ và phản hồi bên ngoài - ở cấp độ ngữ nghĩa của lĩnh vực chủ đề.

---

Внутренняя обратная связь хорошо автоматизируется, поскольку отражает линг-вистические особенности использования языка, адекватно представляемые статистиче-скими характеристиками, построенными на основе частотных показателей БД. В том числе, как показано на рис. 6.4, дистрибутивно-статистический анализ лексики реле-вантных документов позволяет автоматически строить тематико-статистический спектр (ТСС) по теме запроса, используемый системой для ранжирования документов, а структурно-статистический анализ – строить мини-тезаурус9 темы, который может быть использован не только для автоматического лексического расширения выражения запроса, но и в качестве отдельного технологического объекта. Такой мини-тезаурус является структурно-лингвистической моделью предметной области поиска, отражаю-щей не только общепризнанные, но также и актуальные, характерные для проблемной ситуации особенности представления ИП (в том числе, может быть, в первую очередь – новизну подхода пользователя к решаемой им проблеме).

Phản hồi nội bộ được tự động hóa tốt vì nó phản ánh các đặc điểm ngôn ngữ của việc sử dụng ngôn ngữ, được thể hiện đầy đủ bằng các đặc điểm thống kê được xây dựng trên cơ sở các chỉ số tần suất của cơ sở dữ liệu. Bao gồm, như thể hiện trong hình. 6.4, phân tích thống kê phân phối từ vựng của các tài liệu liên quan cho phép bạn tự động xây dựng phổ thống kê theo chủ đề (TSS) về chủ đề truy vấn, được hệ thống sử dụng để xếp hạng tài liệu và phân tích thống kê cấu trúc cho phép bạn xây dựng một phổ thống kê nhỏ từ điển đồng nghĩa9 của chủ đề, có thể được sử dụng không chỉ để mở rộng từ vựng tự động của biểu thức truy vấn mà còn như một đối tượng công nghệ riêng biệt. Một từ điển đồng nghĩa nhỏ như vậy là một mô hình ngôn ngữ-cấu trúc của lĩnh vực chủ đề tìm kiếm, phản ánh không chỉ những đặc điểm được chấp nhận chung mà còn phù hợp, đặc điểm của tình huống có vấn đề, các đặc điểm của cách trình bày IP (có lẽ trước hết bao gồm tính mới của cách tiếp cận của người dùng đối với vấn đề mà anh ta giải quyết).

---

Существование мини-тезауруса в виде операционного объекта обеспечивает также и возможности построения автоматизированных технологий, реализующих внешнюю обратную связь. Мини-тезаурусы, получаемые (и используемые) в итера-тивном процессе поиска по теме запроса, образуют ряд объектов, что позволяет, ис-пользуя дистрибутивно-статистические методы, количественно оценивать динамику процесса и, соответственно, эффективность использованных средств.

Sự tồn tại của một từ điển đồng nghĩa nhỏ dưới dạng một đối tượng vận hành cũng mang lại khả năng xây dựng các công nghệ tự động thực hiện phản hồi bên ngoài. Các từ điển nhỏ thu được (và được sử dụng) trong quá trình lặp đi lặp lại tìm kiếm một chủ đề truy vấn tạo thành một số đối tượng, cho phép sử dụng các phương pháp phân phối và thống kê để đánh giá định lượng động lực của quá trình và theo đó, tính hiệu quả của phương tiện đã sử dụng.

---

В зависимости от способа выбора терминов и характера их использования для развития запроса можно выделить два типа процесса: модификация выражения запроса в том случае, когда запрос представлен в вербальной форме, и реформулировка запро-са, если запрос представлен в кластерной форме. Этот фактор определяет конечность множества типов механизмов поиска.

Tùy thuộc vào phương pháp chọn thuật ngữ và tính chất sử dụng chúng để phát triển truy vấn, có thể phân biệt hai loại quy trình: sửa đổi biểu thức truy vấn trong trường hợp truy vấn được trình bày dưới dạng lời nói và định dạng lại truy vấn nếu truy vấn được trình bày dưới dạng cụm. Yếu tố này quyết định tính hữu hạn của nhiều loại cơ chế tìm kiếm.

---

Поскольку, как отмечалось ранее, принципиально есть две формы представле-ния (выражения) ИП – вербальная и кластерная, каждая из которых отдельно не может быть исключительно полной и точной, механизмы поиска должны быть представлены двумя типами: у первых в качестве запроса используются терминологические ИПЯ-выражения, у вторых – документы.

Vì, như đã lưu ý trước đó, về cơ bản có hai dạng biểu diễn (biểu hiện) IP - bằng lời nói và cụm, mỗi dạng riêng lẻ không thể hoàn chỉnh và chính xác hoàn toàn, nên các cơ chế tìm kiếm phải được trình bày theo hai loại: loại trước sử dụng IP thuật ngữ như một truy vấn -biểu thức, thứ hai - tài liệu.

---

Практически, в зависимости от предполагаемого разнообразия типов поисковых задач и типов интерфейсных технологических объектов, реализация АИПС может включать достаточно разнообразные механизмы поиска. Например, в АИПС IRBIS представлены следующие механизмы поиска. В случае, когда запрос представлен вы-ражением ИПЯ, – это механизм поиска по совпадению терминов, когда поисковый за-прос представляет собой множество терминов, присутствие хотя бы части которых обя-зательно в документе, или механизм поиска по логическому выражению, когда терми-ны связываются логическими операциями, и для принятия решения о релевантности документа необходимо формировать результат вычисления логического выражения. Если же запрос представлен документами, то, в зависимости от типа интерфейсного объекта, мы имеем: в случае отдельного документа – поиск аналогов, если поиск вы-полняется автоматически, а если поисковые термины указываются в документе пользо-вателем – поиск по совпадению терминов. Соответственно, если интерфейсный объект представлен множеством релевантных документов, то в случае, когда система форми-рует словник автоматически, имеем эвристический поиск, а если поисковые термины в сформированном системой словнике указываются пользователем – «поиск по контек-сту».

Trong thực tế, tùy thuộc vào sự đa dạng dự kiến ​​của các loại nhiệm vụ tìm kiếm và loại đối tượng công nghệ giao diện, việc triển khai AIPS có thể bao gồm khá nhiều cơ chế tìm kiếm khác nhau. Ví dụ: IRBIS AIPS cung cấp các cơ chế tìm kiếm sau. Trong trường hợp yêu cầu được thể hiện bằng biểu thức tiếng nước ngoài, đây là cơ chế tìm kiếm bằng cách khớp các thuật ngữ, khi truy vấn tìm kiếm là một tập hợp các thuật ngữ, sự hiện diện của ít nhất một phần trong số đó là bắt buộc trong tài liệu hoặc tìm kiếm cơ chế bằng biểu thức logic, khi các thuật ngữ Chúng tôi được kết nối bằng các phép toán logic và để đưa ra quyết định về mức độ liên quan của tài liệu, cần phải tạo ra kết quả tính toán một biểu thức logic. Nếu yêu cầu được thể hiện bằng tài liệu, thì tùy thuộc vào loại đối tượng giao diện, chúng tôi có: trong trường hợp tài liệu riêng biệt - tìm kiếm tương tự, nếu tìm kiếm được thực hiện tự động và nếu thuật ngữ tìm kiếm được chỉ định trong tài liệu bởi người dùng - tìm kiếm theo cụm từ phù hợp. Theo đó, nếu đối tượng giao diện được biểu thị bằng một tập hợp các tài liệu liên quan, thì trong trường hợp hệ thống tự động tạo từ điển, chúng ta có tìm kiếm heuristic và nếu các thuật ngữ tìm kiếm trong từ điển do hệ thống tạo ra được người dùng chỉ định , chúng tôi có một "tìm kiếm theo ngữ cảnh".

---

Схема основных этапов и технологических средств процесса поиска, позволяющих последовательно локализовать неопределенности перечисленных ранее типов, приведена на рис. 6.4.

Sơ đồ các giai đoạn chính và phương tiện công nghệ của quá trình tìm kiếm, giúp có thể định vị một cách nhất quán những điểm không chắc chắn của các loại được liệt kê trước đó, được hiển thị trong Hình. 6.4.

---

Как было отмечено ранее, задача информационного поиска относится к классу человеко-машинных. Уже на основании того факта, что образ информационной потребности имеет в качестве носителя сознание человека и что именно человек производит сопоставление образа со смысловым содержанием отбираемых документов, а также оценивает адекватность используемых средств и объектов, можно сделать вывод, что система должна предоставлять интерактивный режим для организации гибкого процесса, эффективного в первую очередь с точки зрения человека.

Như đã lưu ý trước đó, nhiệm vụ truy xuất thông tin thuộc về lớp người-máy. Dựa trên thực tế là hình ảnh của nhu cầu thông tin có ý thức của con người với tư cách là người vận chuyển và chính con người so sánh hình ảnh với nội dung ngữ nghĩa của các tài liệu đã chọn, đồng thời đánh giá tính đầy đủ của các phương tiện và đối tượng được sử dụng, chúng tôi có thể kết luận rằng hệ thống cần cung cấp một chế độ tương tác cho tổ chức, quy trình linh hoạt, hiệu quả chủ yếu từ quan điểm con người.

---

Причем на уровне интерфейса такие технологические объекты и инструменты должны быть выделены среди средств поиска и работы с документами, что облегчит пользователю переключение с задачи своей информационно-поисковой деятельности (сбора информации для решения задачи) на «вспомогательную» информационно-управляющую – оценку своих поисковых действий и состояний10.

Hơn nữa, ở cấp độ giao diện, các đối tượng và công cụ công nghệ như vậy cần được nêu bật trong số các phương tiện tìm kiếm và làm việc với tài liệu, điều này sẽ giúp người dùng dễ dàng chuyển từ nhiệm vụ hoạt động truy xuất thông tin của mình (thu thập thông tin để giải quyết vấn đề) cho đến phần quản lý thông tin “phụ trợ” - đánh giá các hành động và trạng thái tìm kiếm của họ10.

```{figure} 6-4.png
Рис. 6.4. Обобщенная схема этапов и средств информационного поиска
```

Представленный на рис. 6.4 итеративный человеко-машинный процесс поиска информации в общем случае является интерактивным и включает следующие этапы:

1) определение темы запроса, ее локализация в предметной области и формали-зация на уровне понятий основной и смежных областей, а также идентификация ресур-са. Здесь система предоставляет систематизированное описание предметной области, а также метаинформирование о тематике, наполнении, структуре и методах доступа к выбранному ресурсу;
2) формирование, а также структурное и лексическое адаптирование выражения запроса, где система предоставляет вспомогательные информационные объекты (сло-вари, тезаурусы, шаблоны и т. д.);
3) отбор документов с помощью одного из механизмов поиска по критерию, адекватному степени неопределенности информационной потребности, где система предоставляет выбор механизма поиска или, например, автоматически с помощью лек-сикографических словарей и проблемно-ориентированных тезаурусов нормирует и расширяет лексику запроса;
4) формирование и управление выдачей найденных документов, где система обеспечивает масштабирование (форматирование) пространства представления выдан-ных документов, а также сортировку и, возможно, рубрицирование или ранжирование по некоторому формальному критерию соответствия, например, с использованием те-матико-статистических распределений, характерных для проблемной области;
5) оценку результата поиска на уровне отдельного документа, где система обес-печивает возможность фиксировать значение степени соответствия запросу пользова-теля и использование лексики документов для непосредственной модификации выра-жения запроса;
6) итоговую оценку результатов поиска на уровне всего запроса или отдельных предложений с точки зрения принятия решения о завершении поискового процесса, где система позволяет количественно оценивать динамику выдач и обеспечивает возмож-ность выборочного обращения к результатам отдельных этапов поиска или формирова-ния проблемно-ориентированных словарей;
7) развитие процесса поиска по технологии реформулирования запроса по об-ратной связи по релевантности или использование каких-либо других ресурсов, напри-мер, ассоциированных БД вторичной или справочной информации, где роль системы – адекватное информирование о такого рода возможностях.

Hiển thị trong hình. 6.4 quá trình tìm kiếm thông tin lặp đi lặp lại của con người và máy móc thường mang tính tương tác và bao gồm các giai đoạn sau:

1) xác định chủ đề của yêu cầu, bản địa hóa nó trong lĩnh vực chủ đề và chính thức hóa ở cấp độ khái niệm về lĩnh vực chính và lĩnh vực liên quan, cũng như xác định nguồn tài nguyên. Ở đây, hệ thống cung cấp mô tả có hệ thống về lĩnh vực chủ đề, cũng như thông tin tổng hợp về chủ đề, nội dung, cấu trúc và phương pháp truy cập vào tài nguyên đã chọn;
2) sự hình thành, cũng như sự điều chỉnh về cấu trúc và từ vựng của biểu thức truy vấn, trong đó hệ thống cung cấp các đối tượng thông tin phụ trợ (từ điển, từ điển đồng nghĩa, mẫu, v.v.);
3) lựa chọn tài liệu bằng cách sử dụng một trong các cơ chế tìm kiếm theo tiêu chí phù hợp với mức độ không chắc chắn của nhu cầu thông tin, trong đó hệ thống cung cấp lựa chọn cơ chế tìm kiếm hoặc, ví dụ, tự động chuẩn hóa và mở rộng từ vựng truy vấn bằng cách sử dụng từ điển từ điển và từ điển đồng nghĩa theo định hướng vấn đề;
4) hình thành và quản lý việc phát hành các tài liệu được tìm thấy, trong đó hệ thống cung cấp khả năng chia tỷ lệ (định dạng) không gian trình bày của các tài liệu đã phát hành, cũng như sắp xếp và có thể phân loại hoặc xếp hạng theo một số tiêu chí tuân thủ chính thức, ví dụ: sử dụng phân phối thống kê theo chủ đề, đặc điểm của khu vực có vấn đề;
5) đánh giá kết quả tìm kiếm ở cấp độ tài liệu riêng lẻ, trong đó hệ thống cung cấp khả năng ghi lại mức độ tuân thủ yêu cầu của người dùng và việc sử dụng từ vựng tài liệu để sửa đổi trực tiếp biểu thức truy vấn;
6) đánh giá cuối cùng về kết quả tìm kiếm ở cấp độ toàn bộ yêu cầu hoặc từng câu riêng lẻ từ quan điểm đưa ra quyết định hoàn tất quá trình tìm kiếm, trong đó hệ thống cho phép đánh giá định lượng về động lực của kết quả tìm kiếm và cung cấp khả năng chọn lọc tham khảo kết quả của các giai đoạn tìm kiếm riêng lẻ hoặc hình thành các từ điển hướng đến vấn đề;
7) phát triển quy trình tìm kiếm bằng cách sử dụng công nghệ cải tiến truy vấn dựa trên phản hồi liên quan hoặc sử dụng bất kỳ tài nguyên nào khác, ví dụ: cơ sở dữ liệu liên quan đến thông tin thứ cấp hoặc tham chiếu, trong đó vai trò của hệ thống là thông tin đầy đủ về loại cơ hội này.

---

Вследствие того, что объект поиска обычно не задан в виде образца, с которым можно соотнести найденный результат, а, с другой стороны, пользовательские ресурсы всегда ограничены, задача организации процесса поиска имеет оптимизационный характер – при временных ограничениях максимизировать показатели выдачи и получить максимальную (субъективную) уверенность в качестве поиска за счет предоставления пользователю в процессе диалога альтернативных направлений, а также количественные и качественные оценки их соответствия запросу.

Do đối tượng tìm kiếm thường không được chỉ định ở dạng mẫu mà kết quả tìm thấy có thể tương quan với nhau, mặt khác, nguồn lực của người dùng luôn bị hạn chế nên nhiệm vụ tổ chức quá trình tìm kiếm là một nhiệm vụ quan trọng. bản chất tối ưu hóa - trong điều kiện hạn chế về thời gian, tối đa hóa kết quả tìm kiếm và đạt được sự tin cậy (chủ quan) tối đa về chất lượng tìm kiếm bằng cách cung cấp cho người dùng các hướng thay thế trong quá trình đối thoại, cũng như các đánh giá định lượng và định tính về việc họ tuân thủ yêu cầu.

---

Отметим еще раз, что здесь имеем два типа обратной связи. Для построения словников на основе лексики документов, определяемых пользователем как истинно релевантные, используется «внешняя» обратная связь. Для построения реформулиро-ванного запроса используется уже «внутренняя» обратная связь, позволяющая выде-лить значимые термины (ранжированием или кластеризацией по статистическим пока-зателям). Соответственно, для построения словников могут использоваться разные ме-тоды, что позволяет, в свою очередь, иметь разные стратегии реформулирования, реа-лизуемые разными технологическими (интерфейсными) средствами.

Hãy để chúng tôi lưu ý một lần nữa rằng chúng tôi có hai loại phản hồi ở đây. Để xây dựng từ điển dựa trên từ vựng của tài liệu được người dùng xác định là thực sự phù hợp, phản hồi “bên ngoài” sẽ được sử dụng. Để xây dựng một truy vấn được định dạng lại, phản hồi “nội bộ” sẽ được sử dụng, cho phép bạn làm nổi bật các thuật ngữ quan trọng (bằng cách xếp hạng hoặc phân cụm theo chỉ số thống kê). Theo đó, các phương pháp khác nhau có thể được sử dụng để xây dựng từ điển, từ đó cho phép có các chiến lược cải cách khác nhau được thực hiện bằng các phương tiện công nghệ (giao diện) khác nhau.

## 6.4. Компоненты информационного поиска

Для обеспечения полноты поискового результата для реальной неодносложной ИП, которая практически всегда многоаспектна и динамична, требуется несколько по-исковых итераций. При этом в случае, если результаты поиска не являются прямым от-ветом истинной потребности (непосредственно решением задачи ОД), то пользователь должен, либо продолжить поиск (в предположении, что полнота предыдущих итераций была недостаточной), либо прекратить поиск в этом ресурсе и обратиться в другой, ли-бо решать задачу ОД самостоятельно.

Để đảm bảo tính đầy đủ của kết quả tìm kiếm cho một IP thực, đa âm tiết, hầu như luôn đa khía cạnh và động, cần phải lặp lại một số lần tìm kiếm. Hơn nữa, nếu kết quả tìm kiếm không phải là phản hồi trực tiếp cho nhu cầu thực sự (giải quyết trực tiếp vấn đề OD), thì người dùng phải tiếp tục tìm kiếm (giả sử rằng tính đầy đủ của các lần lặp lại trước đó là không đủ) hoặc ngừng tìm kiếm trong tài nguyên này và liên hệ với người khác hoặc tự mình giải quyết vấn đề viêm khớp.

---

Только для случая предметного поиска доказательство полноты и непротиворе-чивости является тривиальным: положительный результат поиска (а в этом случае – это идентификатор или адрес описания объекта) и является доказательсвом, так как непо-средственно подтверждает (или опровергает, если выдача была нулевой) существование объекта, обладающего искомыми свойствами. Результат тематического поиска в этом смысле неоднозначен (множественен) и, соответственно, требует последующей систе-матизации – еще одного процедурного шага для упорядочения полученного множества объектов по значениям основания, которое явно не определено. Проблемный поиск, со-ответственно, предполагает уже двухуровневую систематизацию.

Chỉ đối với trường hợp tìm kiếm chủ đề, bằng chứng về tính đầy đủ và nhất quán là không đáng kể: một kết quả tìm kiếm tích cực (và trong trường hợp này, đây là mã định danh hoặc địa chỉ của mô tả đối tượng) là bằng chứng, vì nó trực tiếp xác nhận (hoặc bác bỏ, nếu kết quả là null) sự tồn tại của một đối tượng có các thuộc tính mong muốn. Kết quả của tìm kiếm theo chủ đề theo nghĩa này là không rõ ràng (nhiều) và theo đó, yêu cầu hệ thống hóa tiếp theo - một bước thủ tục khác để sắp xếp tập hợp đối tượng kết quả theo các giá trị của cơ sở, không được xác định rõ ràng. Theo đó, tìm kiếm có vấn đề giả định trước một hệ thống hóa hai cấp độ.

---

При поиске в реальных БД, когда вычислить показатель полноты без просмотра всех документов базы (для определения числа истинно релевантных) невозможно, и развитие процесса поиска, и доказательство его исчерпывающей полноты основывают-ся на процедурной избыточности поисковых компонентов. Действительно в профессио-нальных АИПС обычно предусмотрены и представительная совокупность способов вы-ражения ИП (для компенсации нечеткости лингвистических переменных, используемых в ПОЗе), и несколько поисковых механизмов (за счет разных схем отбора, обеспечива-ющих увеличение комбинативности и размер результатов), и различные процедуры об-работки результатов, обеспечивающих упорядочение и систематизацию результатов.

Khi tìm kiếm trong cơ sở dữ liệu thực, khi không thể tính chỉ số đầy đủ mà không xem tất cả các tài liệu trong cơ sở dữ liệu (để xác định số lượng tài liệu thực sự có liên quan), cả sự phát triển của quá trình tìm kiếm và bằng chứng về tính đầy đủ của nó đều dựa trên về sự dư thừa thủ tục của các thành phần tìm kiếm. Thật vậy, AIPS chuyên nghiệp thường cung cấp một tập hợp các cách thể hiện IP đại diện (để bù đắp cho sự mơ hồ của các biến ngôn ngữ được sử dụng trong POS) và một số cơ chế tìm kiếm (do các sơ đồ lựa chọn khác nhau, đảm bảo tăng khả năng kết hợp và kích thước của kết quả) và các thủ tục khác nhau để xử lý kết quả, đảm bảo trật tự và hệ thống hóa kết quả.

---

Отметим, что дополнительная отдельная во времени обработка требует наличия в системе средств идентификации получаемых объектов (как отдельных элементов, так и их композиций) и средств выборочного использования.

Lưu ý rằng việc xử lý bổ sung theo thời gian riêng biệt yêu cầu hệ thống phải có phương tiện để xác định các đối tượng kết quả (cả các phần tử riêng lẻ và thành phần của chúng) và phương tiện để sử dụng có chọn lọc.

---

Рассмотрим далее основные понятия, относящиеся к поисковому процессу.

Tiếp theo chúng ta hãy xem xét các khái niệm cơ bản liên quan đến quá trình tìm kiếm.

### 6.4.1. Стратегия поиска и классификация АИПС

Поведение пользователя, как организующее начало управления процессом поис-ка, мотивируется не только неопределенностью информационной потребности, но и разнообразием технологических объектов и средств, предоставляемых системой. Одна-ко пока существовал только один класс ИПС, реализующих диалог с одной активной стороной и позволяющих только получать выдачу на запрос (причем пользователя ча-сто не интересовал механизм поиска), о стратегии можно было говорить, имея в виду разве что исследовательские наклонности самого пользователя.

Hành vi của người dùng, với tư cách là sự khởi đầu của tổ chức quản lý quá trình tìm kiếm, được thúc đẩy không chỉ bởi sự không chắc chắn về nhu cầu thông tin mà còn bởi sự đa dạng của các đối tượng và công cụ công nghệ do hệ thống cung cấp. Tuy nhiên, trong khi chỉ có một loại hệ thống thông tin thực hiện đối thoại với một bên tích cực và chỉ được phép nhận kết quả cho một yêu cầu (và người dùng thường không quan tâm đến cơ chế tìm kiếm), có thể nói về chiến lược, chỉ ghi nhớ khuynh hướng nghiên cứu của chính người dùng.

---

В контексте способов организации доступа к информации, представленной в до-кументальной форме, и отдавая должное истории развития ИС, можно говорить о двух типах решений, воплощаемых в промышленных АИПС.

Trong bối cảnh các cách tổ chức quyền truy cập thông tin được trình bày dưới dạng tài liệu và tôn vinh lịch sử phát triển của hệ thống thông tin, chúng ta có thể nói về hai loại giải pháp được thể hiện trong AIPS công nghiệp.

---

Первые – традиционные ИПС, берущие начало от библиотечных систем, инфор-мационный вход в которых реализуется через дополнительные (вторичные по отноше-нию к текстам документов) справочные структуры различного типа.

Đầu tiên là các hệ thống truy xuất thông tin truyền thống, bắt nguồn từ các hệ thống thư viện, thông tin đầu vào được hiện thực hóa thông qua các cấu trúc tham chiếu bổ sung (thứ cấp liên quan đến văn bản tài liệu) thuộc nhiều loại khác nhau.

---

Вторые – гипертекстовые ИС, в которых переход к потенциально полезному до-кументу реализуется через контекстную ссылку, размещенную в тексте самого доку-мента.

Thứ hai là các hệ thống thông tin siêu văn bản, trong đó việc chuyển đổi sang một tài liệu có thể hữu ích được thực hiện thông qua liên kết ngữ cảnh nằm trong chính văn bản của tài liệu đó.

---

Относительная независимость развития этих двух направлений в значительной степени обусловливалась функциональным различием информационного продукта и техническими ограничениями среды хранения. Учитывая тождественность конечной задачи, т. е. обеспечение доступа к реально полезной и полной информации, следует отметить, что гипертекстовые системы использовались в основном для реализации справочных систем, базирующихся на проблемно-ориентированных коллекциях зача-стую слабоструктурированных полнотекстовых документов, а эффективность поиска документов или их фрагментов достигалась через более или менее полную систему контекстно-определенных ссылок. В свою очередь традиционные ИПС предназнача-лись для обработки большого количества однородных (структурно-регулярных), чаще всего вторичных документов небольшой длины.

Sự độc lập tương đối của sự phát triển của hai lĩnh vực này phần lớn được xác định bởi sự khác biệt về chức năng trong sản phẩm thông tin và những hạn chế kỹ thuật của môi trường lưu trữ. Xem xét danh tính của nhiệm vụ cuối cùng, tức là cung cấp quyền truy cập vào thông tin thực sự hữu ích và đầy đủ, cần lưu ý rằng các hệ thống siêu văn bản được sử dụng chủ yếu để triển khai các hệ thống tham chiếu dựa trên các bộ sưu tập hướng đến vấn đề của các tài liệu toàn văn thường có cấu trúc bán cấu trúc và hiệu quả tìm kiếm tài liệu hoặc các đoạn của chúng đạt được thông qua một hệ thống ít nhiều hoàn chỉnh gồm các liên kết theo ngữ cảnh cụ thể. Ngược lại, các hệ thống truy xuất thông tin truyền thống được thiết kế để xử lý một số lượng lớn các tài liệu đồng nhất (có cấu trúc đều đặn), thường là tài liệu thứ cấp có độ dài ngắn.

---

Можно сказать, что для этих двух типов систем пути нахождения пользователем реально нужной информации принципиально различаются.

Chúng ta có thể nói rằng đối với hai loại hệ thống này, cách thức mà người dùng thực sự tìm thấy thông tin mình cần về cơ bản là khác nhau.

---

Координатный принцип индексирования документов и использование в запросе терминов вне контекста предопределяет для ИПС необходимость последующей пользо-вательской оценки некоторого подмножества документов, отобранных системой по формальным признакам.

Nguyên tắc phối hợp của việc lập chỉ mục tài liệu và việc sử dụng các thuật ngữ ngoài ngữ cảnh trong truy vấn xác định trước nhu cầu về hệ thống truy xuất thông tin để người dùng đánh giá tiếp theo một tập hợp con tài liệu nhất định được hệ thống lựa chọn dựa trên tiêu chí hình thức.

---

Гипертекстовые системы позволяют более целенаправленно (хотя лишь в рамках отдельного документа) управлять переходом к следующему документу за счет кон-текстной определенности ссылки. Соответственно, облегчается выработка решения о завершении поиска по критерию удовлетворения потребности или отсутствия новых релевантных документов в последующих выдачах. Однако, по крайней мере, для класса задач поиска новой информации, более эффективным представляется метод координат-ного индексирования, базирующийся на свойстве комбинативности. Кроме того, ли-нейность (одномерность) текста – носителя гипертекстовых ссылок – предполагает од-нозначность навигации, предопределяя переход к единственному документу (может быть, и наилучшему, но в жестко предопределенном контексте). Такого рода навигация в большинстве случаев обеспечивает эффективность подачи информации, однако не да-ет представления о вариантности ситуации и возможных альтернативных или дополни-тельных аспектах.

Các hệ thống siêu văn bản cho phép kiểm soát mục tiêu nhiều hơn (mặc dù chỉ trong một tài liệu) việc chuyển đổi sang tài liệu tiếp theo do tính đặc thù theo ngữ cảnh của liên kết. Theo đó, việc đưa ra quyết định hoàn thành tìm kiếm sẽ dễ dàng hơn dựa trên tiêu chí thỏa mãn nhu cầu hoặc thiếu tài liệu mới liên quan trong các kết quả tìm kiếm tiếp theo. Tuy nhiên, ít nhất đối với loại bài toán tìm kiếm thông tin mới, phương pháp lập chỉ mục tọa độ, dựa trên tính chất tổ hợp, dường như hiệu quả hơn. Ngoài ra, tính tuyến tính (một chiều) của văn bản - vật mang các liên kết siêu văn bản - giả định tính rõ ràng của việc điều hướng, xác định trước việc chuyển đổi sang một tài liệu duy nhất (có lẽ là tốt nhất, nhưng trong một bối cảnh được xác định trước nghiêm ngặt). Kiểu điều hướng này trong hầu hết các trường hợp đảm bảo hiệu quả của việc trình bày thông tin, nhưng không cung cấp ý tưởng về sự thay đổi của tình huống và các khía cạnh thay thế hoặc bổ sung có thể có.

---

В зависимости от формы представления информационной потребности (виду за-проса) и учитывая историю развития ИС, можно выделить два вида «магистральных» направлений поисковых стратегий.

Tùy thuộc vào hình thức trình bày nhu cầu thông tin (loại yêu cầu) và có tính đến lịch sử phát triển của hệ thống thông tin, có thể phân biệt hai loại hướng “chính” của chiến lược tìm kiếm.

---

Большинство промышленных АИПС обеспечивают поддержку традиционной вербальной стратегии, отличительной чертой которой является обязательное построе-ние завершенного, логически и синтаксически правильного выражения, посредством которого может быть получена выдача формально релевантных запросу документов.

Hầu hết các AIPS công nghiệp đều cung cấp hỗ trợ cho chiến lược bằng lời nói truyền thống, đặc điểm nổi bật của chiến lược này là bắt buộc phải xây dựng một biểu thức chính xác, hoàn chỉnh về mặt logic và cú pháp, qua đó có thể thu được các tài liệu có liên quan chính thức đến yêu cầu.

---

Другим видом стратегии является кластерная, обобщающая понятие «документ» или «совокупность документов» до уровня запроса. Такой подход основывается на предположении, что документ, его фрагмент или группа документов может рассматри-ваться не только как результат поиска, но и как средство навигации, т. е. некоторый по-исковый образ. Технологии, поддерживающие кластерные стратегии, в значительной мере позволяют сократить объем просматриваемой при поиске информации за счет определения на основе знаний пользователя групп документов для эффективной иден-тификации его потребностей.

Một loại chiến lược khác là chiến lược cụm, khái quát hóa khái niệm “tài liệu” hoặc “bộ tài liệu” ở cấp độ truy vấn. Cách tiếp cận này dựa trên giả định rằng một tài liệu, đoạn của nó hoặc một nhóm tài liệu có thể được coi không chỉ là kết quả tìm kiếm mà còn là phương tiện điều hướng, tức là một loại hình ảnh tìm kiếm nào đó. Các công nghệ hỗ trợ chiến lược cụm làm giảm đáng kể lượng thông tin được xem trong quá trình tìm kiếm bằng cách xác định các nhóm tài liệu dựa trên kiến ​​thức của người dùng để xác định nhu cầu của họ một cách hiệu quả.

---

В этом смысле сопоставление классических АИПС и гипертекстовых систем сводится не к состоянию конкурирования, а к взаимно не исключающей альтернативно-сти. С появлением же технических возможностей реализации полнотекстовых ИС аль-тернативность выбора «стратегических» технологических решений практически пере-шла в плоскость экономических критериев о степени насыщения документов ссылками и определении пределов размеров словарей для индексирования всех или отдельных полей документов. Наиболее показательным примером является Web-технология Internet, где массивы документов изначально создаются по гипертекстовой технологии, а в дальнейшем строятся индексы, реализующие «классические» технологии ИПС.

Theo nghĩa này, việc so sánh các hệ thống AIPS cổ điển và siêu văn bản không phải là tình trạng cạnh tranh mà là một sự thay thế không loại trừ lẫn nhau. Với sự ra đời của năng lực kỹ thuật triển khai IS toàn văn, sự lựa chọn thay thế các giải pháp công nghệ “chiến lược” trên thực tế đã chuyển sang mặt phẳng tiêu chí kinh tế về mức độ bão hòa của tài liệu có liên kết và xác định giới hạn về kích thước của từ điển để lập chỉ mục tất cả hoặc từng trường tài liệu. Ví dụ minh họa nhất là công nghệ Internet Web, trong đó các mảng tài liệu ban đầu được tạo bằng công nghệ siêu văn bản, sau đó các chỉ mục được xây dựng để triển khai các công nghệ truy xuất thông tin “cổ điển”.

### 6.4.2. Методы поиска

Методы поиска, как средства выделения подмножества документов, потенци-ально содержащих описание решения задачи ОД, являются отражением процесса нахождения решения и зависят от характера задачи и предметной области.

Các phương pháp tìm kiếm, như một phương tiện để xác định một tập hợp con các tài liệu có khả năng chứa mô tả giải pháp cho vấn đề OA, là sự phản ánh của quá trình tìm giải pháp và phụ thuộc vào bản chất của vấn đề và lĩnh vực chủ đề.

---

Если не рассматривать семантические проблемы смысловыражения, оптимиза-ционная задача АИС – это минимизация совокупных временных затрат за счет сниже-ния суммарного объема выдач, просматриваемых потребителем. Методы сокращения пространства перебора (просматриваемого подмножества) образуют по существу мето-дологическую основу стратегии поиска и могут быть разделены на следующие классы:

- методы поиска в одном пространстве (обычно, тематическом);
- методы поиска в иерархически упорядоченном пространстве;
- методы поиска в альтернативных пространствах;
- методы поиска в динамическом пространстве (изменяющемся в процессе по-иска).

Nếu chúng ta không xem xét các vấn đề về ngữ nghĩa của biểu thức ngữ nghĩa thì nhiệm vụ tối ưu hóa của AIS là giảm thiểu tổng chi phí thời gian bằng cách giảm tổng khối lượng kết quả tìm kiếm được người tiêu dùng xem. Các phương pháp giảm không gian tìm kiếm (tập hợp con được tìm kiếm) về cơ bản là cơ sở phương pháp luận của chiến lược tìm kiếm và có thể được chia thành các lớp sau:

- phương pháp tìm kiếm trong một không gian (thường theo chủ đề);
- phương pháp tìm kiếm trong không gian được sắp xếp theo thứ bậc;
- phương pháp tìm kiếm trong không gian thay thế;
- phương pháp tìm kiếm trong không gian động (thay đổi trong quá trình tìm kiếm).

---

Для случая документальных ретроспективных БД наиболее актуальными явля-ются два первых случая, где в свою очередь можно выделить следующие подклассы:

- поиск методом уточнения/расширения области;
- поиск с использованием абстрактных пространств (динамически выделяемых в соответствии с некоторым фиксированным набором признаков);
- поиск с использованием метапространства (динамическое определение набо-ра признаков для выделения подпространств), т. е. с переопределением мето-да поиска.

Đối với trường hợp cơ sở dữ liệu hồi cứu tài liệu, liên quan nhất là hai trường hợp đầu tiên, trong đó có thể phân biệt các phân lớp sau:

- Tìm kiếm bằng phương pháp làm rõ/mở rộng địa bàn;
- tìm kiếm bằng cách sử dụng không gian trừu tượng (được phân bổ động theo một số bộ tính năng cố định);
- tìm kiếm bằng cách sử dụng siêu không gian (xác định động một tập hợp các tính năng để xác định các không gian con), tức là với việc xác định lại phương pháp tìm kiếm.

---

Учитывая опосредованность процесса извлечения информации из БД, можно сказать, что практически всегда процесс выполняется в два этапа (что соответствует и числу сторон – участников процесса). Первый этап – автоматизированный отбор доку-ментов по формальному критерию, в той или иной степени полно и точно соответству-ющих информационной потребности (предпочтительно более полно, хотя и менее точ-но), и второй – «ручной» отбор с непосредственным просмотром.

Xem xét tính chất gián tiếp của quá trình trích xuất thông tin từ cơ sở dữ liệu, chúng ta có thể nói rằng quá trình này hầu như luôn được thực hiện theo hai giai đoạn (cũng tương ứng với số lượng các bên tham gia vào quy trình). Giai đoạn đầu tiên là lựa chọn tự động các tài liệu theo tiêu chí hình thức, ở mức độ này hay mức độ khác tương ứng đầy đủ và chính xác với nhu cầu thông tin (tốt nhất là đầy đủ hơn, mặc dù kém chính xác hơn), và giai đoạn thứ hai là lựa chọn “thủ công” với xem trực tiếp.

---

К методам поиска необходимо относить все функциональные решения – от ме-тодов сопоставления ПОЗ и отбора документов по некоторому критерию смыслового соответствия (КСС) до методов упорядочивания документов в выдаче, включая исполь-зование результатов поиска для реформулирования запроса.

Các phương pháp tìm kiếm phải bao gồm đầy đủ các giải pháp chức năng - từ phương pháp so sánh POS và lựa chọn tài liệu theo một tiêu chí tương ứng ngữ nghĩa (SCC) nhất định đến các phương pháp tổ chức tài liệu trong kết quả tìm kiếm, bao gồm cả việc sử dụng kết quả tìm kiếm để định dạng lại truy vấn.

#### 6.4.2.1. Отбор документов по формальным критериям

Понятие метода отбора документов по существу сводится к понятию критерия смыслового соответствия. По признаку использования мер близости (полному или ча-стичному совпадению поисковых образов) методы можно разделить на две группы.

Khái niệm về phương pháp lựa chọn tài liệu về cơ bản bắt nguồn từ khái niệm tiêu chí về sự tương ứng ngữ nghĩa. Dựa trên việc sử dụng các thước đo độ gần (trùng khớp hoàn toàn hoặc một phần của hình ảnh tìm kiếm), các phương pháp có thể được chia thành hai nhóm.

---

Методы первой группы в основном используются для реализации традиционно-го поиска по булеву выражению.

Các phương pháp của nhóm đầu tiên chủ yếu được sử dụng để thực hiện tìm kiếm truyền thống bằng biểu thức Boolean.

---

Второй группе соответствуют многочисленные реализации формальных моде-лей, таких как поиск, использующий векторные меры близости; весовой поиск и поиск по нечетким множествам; кластерный поиск; сетевые модели и модель распространя-ющихся активизаций (к последним также можно отнести модель детерминированного гипертекста).

Nhóm thứ hai tương ứng với nhiều triển khai của các mô hình hình thức, chẳng hạn như tìm kiếm bằng cách sử dụng các độ đo lân cận của vectơ; tìm kiếm có trọng số và tìm kiếm tập mờ; tìm kiếm cụm; mô hình mạng và mô hình lan truyền kích hoạt (mô hình sau cũng bao gồm mô hình siêu văn bản xác định).

---

Упомянутые методы достаточно хорошо проработаны и широко распространены для ИПЯ дескрипторного типа, когда смыслообразующей единицей является слово естественного (в том числе и нормализованного) или искусственного (например, клас-сификационного) языка. То есть сопоставляемыми в критерии объектами являются подмножества семантически связанных дескрипторов, в совокупности обозначающие характерные признаки объекта и таким образом позволяющие реконструировать его об-раз.

Các phương pháp được đề cập được phát triển khá tốt và phổ biến đối với FL thuộc loại mô tả, khi đơn vị hình thành nghĩa là một từ của ngôn ngữ tự nhiên (bao gồm cả ngôn ngữ chuẩn hóa) hoặc nhân tạo (ví dụ: phân loại). Nghĩa là, các đối tượng được so sánh trong tiêu chí là tập hợp con của các bộ mô tả có liên quan về mặt ngữ nghĩa, chúng chỉ định chung các đặc điểm đặc trưng của đối tượng và do đó có thể tái tạo lại hình ảnh của nó.

---

Несколько иные возможности предоставляют языки описания данных (и, воз-можно, некоторые ИПЯ), которые позволяют включать в качестве информационных компонентов такие поисковые средства, как явные или опосредованные ссылки на документы или их подмножества. Наиболее распространенными примерами являются ги-пертекстовые структуры, в которых можно выделить следующие структурно-технологические решения реализации ссылок:

- непосредственные ссылки – детерминированный гипертекст, связывающий в явной форме фрагмент одного документа с другим документом;
- опосредованные ссылки, устанавливаемые динамически, например, через не-который нормализованный словарь или словарь поискового поля;
- динамически разрешаемые ссылки, определяемые поисковой функцией в контексте семантического поля документа или кластера документов.

Các khả năng khác nhau được cung cấp bởi các ngôn ngữ mô tả dữ liệu (và có thể là một số IPL), cho phép bạn bao gồm các thành phần thông tin như các công cụ tìm kiếm dưới dạng liên kết rõ ràng hoặc gián tiếp đến tài liệu hoặc tập hợp con của chúng. Các ví dụ phổ biến nhất là cấu trúc siêu văn bản, trong đó có thể phân biệt các giải pháp cấu trúc và công nghệ sau để triển khai liên kết:

- liên kết trực tiếp – siêu văn bản xác định liên kết rõ ràng một đoạn của tài liệu này với một tài liệu khác;
- các liên kết gián tiếp được thiết lập động, ví dụ, thông qua một số từ điển chuẩn hóa hoặc từ điển trường tìm kiếm;
- các liên kết được giải quyết động được xác định bởi chức năng tìm kiếm trong ngữ cảnh trường ngữ nghĩa của một tài liệu hoặc cụm tài liệu.

#### 6.4.2.2. Методы построения поискового образа запроса

Выбранные КСС в сочетании с языковыми средствами определяют способ пред-ставления информации в АИС и таким образом предопределяют методы построения ПОЗ. Однако значительное влияние имеет и характер цели (объекта) поиска. Можно было бы считать, что это влияние должно полностью учитываться на стадии выбора КСС и проектирования информационного и лингвистического обеспечения, однако для такой системы, как документальная БД, можно говорить только о возможном преобла-дании (статистически) какого-то типа неопределенности. То есть реализуемый метод построения ПОЗ должен обеспечивать более или менее эффективные способы построе-ния запроса для достижения целей различного типа.

CSS được chọn kết hợp với các phương tiện ngôn ngữ sẽ xác định cách trình bày thông tin trong AIS và do đó xác định trước các phương pháp xây dựng POS. Tuy nhiên, bản chất của mục tiêu (đối tượng) tìm kiếm cũng có ảnh hưởng đáng kể. Người ta có thể cho rằng ảnh hưởng này cần được tính đến đầy đủ ở giai đoạn lựa chọn CSS và thiết kế hỗ trợ thông tin và ngôn ngữ, tuy nhiên, đối với một hệ thống như cơ sở dữ liệu tài liệu, người ta chỉ có thể nói về ưu thế có thể có (về mặt thống kê) của một số loại sự không chắc chắn. Nghĩa là, phương pháp được triển khai để xây dựng POS phải cung cấp ít nhiều cách hiệu quả để xây dựng truy vấn nhằm đạt được các mục tiêu thuộc nhiều loại khác nhau.

---

В соответствии с приведенной ранее типологией «чистых» стратегий поиска рас-смотрим особенности методов построения запроса.

Theo kiểu chữ của các chiến lược tìm kiếm “thuần túy” được đưa ra trước đó, chúng ta hãy xem xét các đặc điểm của phương pháp xây dựng truy vấn.

---

Стратегии, определенные как вербальные, ориентированы на структурные мето-ды построения запроса, когда объект поиска достаточно хорошо определяется как из-вестной, так и неизвестной стороной. Этому соответствуют поисковые ситуации, когда субъекту поиска известен аналог или предмет поиска хорошо определяется в системе понятий предметной области.

Các chiến lược được xác định bằng lời nói tập trung vào các phương pháp cấu trúc để xây dựng truy vấn, khi đối tượng tìm kiếm được xác định đầy đủ bởi cả bên đã biết và bên chưa biết. Điều này tương ứng với các tình huống tìm kiếm khi chủ đề tìm kiếm biết một từ tương tự hoặc chủ đề tìm kiếm được xác định rõ ràng trong hệ thống khái niệm về lĩnh vực chủ đề.

---

В этом случае процесс построения запроса основывается на структуризации объ-екта и смежных областей, построении сети понятий и дальнейшей редукции синтагма-тических связей между понятиями к отношению «совместной встречаемости».

Trong trường hợp này, quá trình xây dựng truy vấn dựa trên cấu trúc của đối tượng và các lĩnh vực liên quan, việc xây dựng mạng lưới các khái niệm và tiếp tục giảm bớt các kết nối ngữ đoạn giữa các khái niệm thành mối quan hệ “đồng xảy ra”.

---

Традиции естественно-научной систематизации, основанные на построении дре-вовидных структур, обусловливают «естественность» построения дерева понятий, хо-рошо определяемого логическими выражениями, где в качестве операндов используют-ся наименования понятий, которые в свою очередь достаточно просто обозначаются ло-гически-подобными выражениями в рамках конкретного ИПЯ.

Truyền thống hệ thống hóa khoa học tự nhiên, dựa trên việc xây dựng các cấu trúc dạng cây, xác định tính “tự nhiên” của việc xây dựng một cây khái niệm, được xác định rõ ràng bằng các biểu thức logic, trong đó tên của các khái niệm được sử dụng làm toán hạng, do đó khá được chỉ định một cách hợp lý các biểu thức tương tự trong một IP cụ thể.

---

Такой «естественный» и методически завершенный процесс реализуется следу-ющими шагами (соответствующими уровням представления объекта):

- формированием понятийного образа с выделением основных и ассоциатив-ных понятий (аналог, смежный, противоположный);
- построением дерева (сети) понятий;
- нормализацией сети понятий и редуцированием связей до «совместной встречаемости»;
- терминологическим (естественно-научным) определением понятий;
- обозначением терминологических определений понятий средствами ИПЯ.

Một quy trình “tự nhiên” và được hoàn thiện một cách có phương pháp như vậy được thực hiện theo các bước sau (tương ứng với các cấp độ biểu diễn đối tượng):

- hình thành một hình ảnh khái niệm với việc xác định các khái niệm cơ bản và liên kết (tương tự, liền kề, đối diện);
- xây dựng cây (mạng lưới) các khái niệm;
- bình thường hóa mạng lưới các khái niệm và giảm các kết nối thành “đồng thời”;
- định nghĩa thuật ngữ (khoa học tự nhiên) của các khái niệm;
- chỉ định các định nghĩa thuật ngữ của các khái niệm sử dụng FL.

---

Кластерные стратегии тяготеют к построению «собирательного образа» некото-рой части предметной области, границы которой либо предопределены при создании БД (чаще всего реализованы в виде систематических указателей к массивам), либо определяются динамически в процессе поиска.

Chiến lược cụm có xu hướng xây dựng một “hình ảnh tập thể” về một phần nào đó của lĩnh vực chủ đề, ranh giới của chúng được xác định trước khi tạo cơ sở dữ liệu (thường được triển khai dưới dạng con trỏ hệ thống tới mảng) hoặc được xác định động trong quá trình tìm kiếm .

---

В этом случае процесс построения запроса почти сливается с процессом постро-ения выдачи, т. е. отсутствует явная граница – момент, до которого формируется запрос (например, поисковое предложение) и после которого выполняется отбор документов из БД по критерию соответствия. В качестве запроса могут выступать как отдельный документ, так и кластеры документов, а отбор производится «по подобию» – близости (схожести) формы или содержания.

Trong trường hợp này, quá trình xây dựng truy vấn gần như hợp nhất với quá trình xây dựng kết quả tìm kiếm, tức là không có ranh giới rõ ràng - thời điểm trước khi truy vấn được tạo (ví dụ: câu tìm kiếm) và sau đó tài liệu được tạo ra. được chọn từ cơ sở dữ liệu theo tiêu chí phù hợp. Truy vấn có thể là một tài liệu đơn lẻ hoặc các cụm tài liệu và việc lựa chọn được thực hiện “theo mức độ tương tự” - mức độ gần gũi (tương tự) về hình thức hoặc nội dung.

---

В простейшем (но наиболее распространенном) случае основой для построения мер близости являются дискретные модели, опирающиеся на понятие множества (тер-минов и документов). Именно термины и документы в отдельности или их упорядочен-ные подмножества являются технологическими, интерфейсными объектами, обеспечи-вающими возможность управления поиском.

Trong trường hợp đơn giản nhất (nhưng phổ biến nhất), cơ sở để xây dựng các thước đo độ gần là các mô hình rời rạc dựa trên khái niệm về một tập hợp (thuật ngữ và tài liệu). Chính các thuật ngữ và tài liệu riêng lẻ hoặc các tập hợp con được sắp xếp theo thứ tự của chúng là các đối tượng giao diện, công nghệ cung cấp khả năng kiểm soát việc tìm kiếm.

---

Управление процессом поиска, начинающегося с любого, может быть, самого простейшего вхождения в предметную область (например, через иерархический указа-тель), построено по принципу «обратной связи» [Сэлтон, 1973], когда каждая выдача системы (как термины, так и документы) оценивается на соответствие теме и использу-ется в качестве запроса для следующей итерации отбора – так называемый метод ре-формулирования запроса по обратной связи.

Việc kiểm soát quá trình tìm kiếm, có lẽ bắt đầu từ bất kỳ mục nhập đơn giản nhất nào vào lĩnh vực chủ đề (ví dụ: thông qua chỉ mục phân cấp), được xây dựng dựa trên nguyên tắc “phản hồi” [Salton, 1973], khi mỗi đầu ra của hệ thống (cả thuật ngữ và tài liệu) được đánh giá về mức độ liên quan đến chủ đề và được sử dụng làm yêu cầu cho lần lựa chọn tiếp theo - cái gọi là phương pháp cải tiến yêu cầu phản hồi.

---

Для «простых поисков» (и «простых» пользователей) кластерные стратегии эф-фективны чаще всего за счет простоты представления массива, предопределенного иерархиями классификаций, рубрикаций и указателей ПрО.

Đối với “tìm kiếm đơn giản” (và người dùng “đơn giản”), chiến lược cụm thường hiệu quả nhất do tính đơn giản trong việc biểu thị một mảng được xác định trước bởi hệ thống phân cấp, bảng tự đánh giá và chỉ mục SbA.

---

Для сложных поисков с высокой степенью неопределенности объекта поиска кластерные стратегии, не требующие предварительного построения точного выраже-ния, позволяют выделить кластеры, содержащие нужные документы. Кроме того, эше-лонирование выдач обеспечивает пользователя дополнительной информацией, позво-ляющей формулировать более объективные оценки качества поиска и, соответственно, иметь более обоснованные решения о завершении процесса поиска.

Đối với các tìm kiếm phức tạp có mức độ không chắc chắn cao về đối tượng tìm kiếm, các chiến lược cụm, không yêu cầu xây dựng sơ bộ biểu thức chính xác, có thể chọn các cụm chứa các tài liệu cần thiết. Ngoài ra, việc xếp hạng các kết quả tìm kiếm còn cung cấp cho người dùng thông tin bổ sung cho phép họ đưa ra các đánh giá khách quan hơn về chất lượng tìm kiếm và theo đó, đưa ra quyết định sáng suốt hơn về việc hoàn tất quá trình tìm kiếm.

#### 6.4.2.3. Методы обработки результатов поиска

По характеру преобразований (в контексте дальнейшего использования резуль-татов обработки) методы обработки результатов поиска можно условно разделить на две группы:

- структурно-форматные преобразования;
- структурно-семантические преобразования (информационно-аналитические, логико-семантические).

Dựa trên bản chất của các phép biến đổi (trong bối cảnh tiếp tục sử dụng kết quả xử lý), các phương pháp xử lý kết quả tìm kiếm có thể được chia thành hai nhóm:

- chuyển đổi cấu trúc và định dạng;
- các biến đổi cấu trúc-ngữ nghĩa (thông tin-phân tích, logic-ngữ nghĩa).

---

Структурно-форматные преобразования обеспечивают необходимое разнооб-разие форм представления информации как на уровне отдельных документов, так и на уровне их совокупностей.

Các chuyển đổi cấu trúc và định dạng cung cấp nhiều hình thức cần thiết để trình bày thông tin ở cả cấp độ tài liệu riêng lẻ và cấp độ tổng hợp của chúng.

---

Такие преобразования реализуются:

- методами, обеспечивающими селективность выбора данных на уровне полей и агрегатов данных – внутри документа, и на уровне помеченных подмно-жеств документов – внутри совокупности наборов документов (например, выдач по отдельным запросам);
- методами представления (пространственного размещения) информации, включая методы «масштабирования» – возможностью иметь сокращенную форму, позволяющую свернуть, например, документ до одной строки, а вы-дачу – до одного экрана, обеспечивая локализацию области восприятия ин-формации и создавая некоторую «образность»;
- методами упорядочивания как по структурным параметрам (например, зна-чениям отдельных полей документов), так и по семантически значимым па-раметрам, например мерам близости в пространстве «термин-термин» или «документ-документ».

Những chuyển đổi như vậy được thực hiện:

- các phương pháp đảm bảo tính chọn lọc của việc lựa chọn dữ liệu ở cấp độ trường và tập hợp dữ liệu - trong một tài liệu và ở cấp độ tập hợp con được gắn nhãn của tài liệu - trong một tập hợp các bộ tài liệu (ví dụ: kết quả cho các yêu cầu riêng lẻ);
- các phương pháp trình bày (vị trí không gian) thông tin, bao gồm cả các phương pháp "chia tỷ lệ" - khả năng có dạng viết tắt cho phép, ví dụ, một tài liệu được rút gọn thành một dòng và xuất ra một màn hình, đảm bảo bản địa hóa lĩnh vực nhận thức thông tin và tạo ra một số “ hình ảnh”;
- phương pháp sắp xếp cả theo tham số cấu trúc (ví dụ: giá trị của các trường tài liệu riêng lẻ) và theo tham số có ý nghĩa về mặt ngữ nghĩa, ví dụ: thước đo mức độ gần nhau trong không gian “thuật ngữ” hoặc “tài liệu-tài liệu”.

---

Структурно-семантические преобразования должны обеспечить пользователя (субъекта управления процессом поиска) информацией, необходимой для развития процесса поиска, например, путем реформулировки запроса по обратной связи или ин-формацией для принятия обоснованного решения о достаточности полученного резуль-тата или прекращении процесса по причине несоответствия профиля БД теме запроса.

Các chuyển đổi ngữ nghĩa-cấu trúc phải cung cấp cho người dùng (chủ đề quản lý quy trình tìm kiếm) thông tin cần thiết để phát triển quy trình tìm kiếm, ví dụ: bằng cách định dạng lại yêu cầu phản hồi hoặc thông tin để đưa ra quyết định sáng suốt về tính đầy đủ của kết quả thu được hoặc chấm dứt quá trình do hồ sơ không khớp với chủ đề DB của yêu cầu.

---

Соответственно, эти методы можно разделить на две группы:

- информационно-аналитические, т. е. обобщающие результаты, например по-строением распределений, статистически характеризующих выдачу или мно-жество терминов. Такие количественные характеристики могут использо-ваться для принятия решения «в целом» (как внешняя независимая статисти-ческая экспертиза);
- логико-семантические, т. е. обеспечивающие межуровневые преобразования информации (например, преобразования лексики документов некоторого се-мантически связного кластера в кластеры ранжированных словников).

Theo đó, các phương pháp này có thể được chia thành hai nhóm:

- phân tích thông tin, tức là khái quát hóa các kết quả, ví dụ bằng cách xây dựng các phân bố có đặc tính thống kê đặc trưng cho đầu ra hoặc một tập hợp các thuật ngữ. Những đặc điểm định lượng như vậy có thể được sử dụng để đưa ra quyết định “nói chung” (như một cuộc kiểm tra thống kê độc lập bên ngoài);
- logic-ngữ nghĩa, tức là cung cấp các chuyển đổi thông tin giữa các cấp độ (ví dụ: chuyển đổi từ vựng của các tài liệu của một số cụm mạch lạc về mặt ngữ nghĩa thành các cụm từ điển được xếp hạng).

---

Поисковые методы, таким образом, образуют интерфейсный слой, а при проек-тировании программного обеспечения АИПС определяют требования к «внутриси-стемным» методам организации и поиска данных.

Do đó, các phương pháp tìm kiếm tạo thành một lớp giao diện và khi thiết kế phần mềm AIPS, chúng xác định các yêu cầu đối với các phương pháp tổ chức và truy xuất dữ liệu “trong hệ thống”.

#### 6.4.2.4. Методы управления поиском

Для того чтобы дать пользователю возможность оценить полноту полученного результата (по сути, возможность управлять процессом поиска), необходимо предоставить специальные инструменты, позволяющие обращаться к ранее полученным объектам и результатам. На уровне интерфейса эти объекты должны быть отделены от средств поиска и работы с документами, чтобы пользователю проще было переключаться с задачи своей основной деятельности (сбора информации для решения задачи) на проблемы оценки своих действий и состояний.

Để giúp người dùng có cơ hội đánh giá tính đầy đủ của kết quả thu được (trên thực tế là khả năng kiểm soát quá trình tìm kiếm), cần cung cấp các công cụ đặc biệt cho phép truy cập vào các đối tượng và kết quả thu được trước đó. Ở cấp độ giao diện, các đối tượng này cần được tách biệt khỏi phương tiện tìm kiếm và làm việc với tài liệu, để người dùng dễ dàng chuyển từ nhiệm vụ hoạt động chính của mình (thu thập thông tin để giải quyết vấn đề) sang các vấn đề đánh giá. hành động và trạng thái của mình.

---

Для оценки динамики эффективности процесса поиска дистрибутивно-статистическими методами необходимо, чтобы все этапы технологии относились к одному (семантическому однородному) пространству объектов (т. е. задача не должна быть многокритериальной). Иначе говоря, результаты, получаемые на разных этапах и, соответственно, по разным поисковым образам, должны относиться к одному исходному (семантически замкнутому) запросу, который как предмет поиска представляет тематически отдельную реальную информационную потребность пользователя. То есть в этом случае оценивается эффективность уже поискового образа запроса, а повышение эффективности поискового процесса основывается на последовательном повышении эффективности ПОЗ по отношению к предшествующему варианту (которая может определяться на основе, например, корреляционного анализа подмножеств $\{ T_1, T_2, \ldots, T_n \}$ и $\{ D_1, D_2, \ldots, D_n \}$, введенных в гл. 4).

Để đánh giá tính năng động của hiệu quả của quá trình tìm kiếm bằng phương pháp thống kê phân phối, điều cần thiết là tất cả các giai đoạn của công nghệ phải thuộc về cùng một không gian (đồng nhất về mặt ngữ nghĩa) của các đối tượng (nghĩa là nhiệm vụ không được đa tiêu chí). Nói cách khác, các kết quả thu được ở các giai đoạn khác nhau và theo đó, từ các hình ảnh tìm kiếm khác nhau phải liên quan đến một truy vấn ban đầu (đóng về mặt ngữ nghĩa), truy vấn này, với tư cách là một chủ đề tìm kiếm, thể hiện nhu cầu thông tin thực sự riêng biệt theo chủ đề của người dùng. Nghĩa là, trong trường hợp này, hiệu quả của hình ảnh tìm kiếm của truy vấn được đánh giá và việc tăng hiệu quả của quá trình tìm kiếm dựa trên sự gia tăng nhất quán về hiệu quả của POZ so với phiên bản trước đó (có thể được xác định trên cơ sở, ví dụ, phân tích tương quan của các tập con $\{ T_1, T_2, \ldots, T_n \}$ và $\{ D_1, D_2, \ldots, D_n \}$, được giới thiệu ở Chương 4).

---

Для реальных запросов, которые практически являются многоаспектными и включают несколько подтем, общий результат будет получен последовательностью фактически самостоятельных (завершенных с точки зрения получения и оценки результатов) вышеописанных многоэтапных процессов поиска, каждый из которых должен быть выполнен для каждой подтемы и аспекта. То есть, как это представлено на рис. 6.6, каждому отдельному элементу тематически-аспектной декомпозиции запроса, представляющей информационную потребность как семантически значимый объект поиска на логическом уровне, соответствует отдельный физический процесс поиска и результат. При этом в реальных ИПС результаты поиска по отдельным этапам последовательно фиксируются в протоколе, позволяющем отобразить ход процесса и, возможно, на следующих этапах обратиться к ранее полученным результатам.

Đối với các truy vấn thực tế, có tính chất đa khía cạnh và bao gồm một số chủ đề phụ, kết quả tổng thể sẽ thu được bằng một chuỗi các quy trình tìm kiếm gồm nhiều bước gần như độc lập (hoàn chỉnh về mặt thu thập và đánh giá kết quả) được mô tả ở trên, mỗi trong số đó phải được thực hiện cho từng chủ đề và khía cạnh phụ. Đó là, như thể hiện trong hình. 6.6, mỗi phần tử riêng lẻ của việc phân rã theo khía cạnh chủ đề của một truy vấn, thể hiện nhu cầu thông tin như một đối tượng tìm kiếm có ý nghĩa về mặt ngữ nghĩa ở cấp độ logic, tương ứng với một kết quả và quy trình tìm kiếm vật lý riêng biệt. Đồng thời, trong các hệ thống truy xuất thông tin thực, kết quả tìm kiếm cho các giai đoạn riêng lẻ được ghi tuần tự trong một giao thức, giúp hiển thị tiến trình của quá trình và có thể ở các giai đoạn tiếp theo, tham khảo các kết quả thu được trước đó.

---

Однако, предопределенная требованием оцениваемости, изолированность объекта поиска и, соответственно, результатов, на практике трудно достижима: множество документов, выданных при поиске по одному аспекту, обычно содержит документы, относящиеся и к другим аспектам. И, кроме того, в многоэтапном процессе развития запроса пользователь, получая значимый или просто интересный документ, но относящийся к другому аспекту, обычно переключает внимание именно на него и, соответственно, выходит за пределы тематически замкнутого пространства, что нарушает требование однородности и снижает эффективность поиска.

Tuy nhiên, do yêu cầu về tính đánh giá, sự cô lập của đối tượng tìm kiếm và do đó, kết quả khó đạt được trong thực tế: tập tài liệu trả về trong quá trình tìm kiếm một khía cạnh thường chứa các tài liệu liên quan đến các khía cạnh khác. Ngoài ra, trong quá trình phát triển truy vấn nhiều giai đoạn, người dùng, khi nhận được một tài liệu quan trọng hoặc đơn giản là thú vị, nhưng liên quan đến một khía cạnh khác, thường chuyển sự chú ý sang tài liệu đó và theo đó, vượt ra ngoài không gian khép kín theo chủ đề, vi phạm yêu cầu về tính đồng nhất và làm giảm hiệu quả tìm kiếm.

---

Это означает, что представление процесса поиска на физическом уровне (последовательность получения результата, зафиксированная в протоколе в виде интерфейсных объектов) не будет соответствовать последовательности на логическом уровне. Для обеспечения соответствия вводится промежуточный интерфейсный уровень представления процесса поиска. Объекты этого уровня (и характер их представления, например, упорядочение) структурно будут соответствовать логическому уровню, и каждый из них будет представлять (объединять) элементы (ПОЗ, словники, результаты поиска), относящиеся к соответствующему предмету поиска, но физически полученные, возможно, на разных этапах.

Điều này có nghĩa là việc biểu diễn quá trình tìm kiếm ở cấp độ vật lý (trình tự thu được kết quả, được ghi trong giao thức dưới dạng đối tượng giao diện) sẽ không tương ứng với trình tự ở cấp độ logic. Để đảm bảo sự tuân thủ, mức giao diện trung gian để thể hiện quá trình tìm kiếm được giới thiệu. Các đối tượng ở cấp độ này (và tính chất biểu diễn của chúng, chẳng hạn như thứ tự) sẽ tương ứng về mặt cấu trúc với cấp độ logic và mỗi đối tượng sẽ đại diện (kết hợp) các phần tử (POZ, từ điển, kết quả tìm kiếm) liên quan đến chủ đề tìm kiếm tương ứng, nhưng có lẽ thu được về mặt vật chất ở các giai đoạn khác nhau.

```{figure} 6-6.png
Рис. 6.6. Уровневая модель поискового процесса
```

Тем самым, на передний план выдвигается проблема организации взаимодействия пользователя с системой в процессе поиска.

Như vậy, vấn đề tổ chức tương tác của người dùng với hệ thống trong quá trình tìm kiếm được đặt ra.

---

И если для процесса в целом (с точки зрения конечного пользователя) имеем всего два типа основных операционных объектов – запрос (как пользовательское представление ИП) и документ (как семантически целостный ответ или его часть, сформированный системой – отображение запроса в пространство документов), то с точки зрения организации процесса взаимодействия интерфейс системы должен иметь разнообразные объекты. При этом разнообразие типов объектов пользовательского интерфейса определяется «развитостью» технологических и процедурных возможностей системы. Для случая обобщенной схемы, технологически обеспечивающей снятие информационной неопределенности всех типов, такими объектами являются:

- тезаурусы, обеспечивающие ориентацию пользователя в предметной области;
- словари поисковой системы, используемые для формирования поискового выражения;
- тематические словники, представляющие информативную лексику предметной области.
Эти объекты, являясь технологически вспомогательными, используются на разных этапах поиска и обеспечивают возможность более или менее адекватного выражения информационной потребности пользователя. При этом для отражения индивидуальных особенностей ИП они, как интерфейсные объекты, не могут быть эффективно использованы, поскольку, вследствие усредненной природы, представляют ПрО в целом.

Và nếu đối với toàn bộ quá trình (theo quan điểm của người dùng cuối), chúng ta chỉ có hai loại đối tượng hoạt động chính - một yêu cầu (dưới dạng biểu thị IP của người dùng) và một tài liệu (dưới dạng phản hồi tích hợp về mặt ngữ nghĩa hoặc một phần do hệ thống tạo ra - ánh xạ yêu cầu vào không gian tài liệu), thì trên quan điểm tổ chức quá trình tương tác, giao diện hệ thống phải có nhiều đối tượng đa dạng. Đồng thời, sự đa dạng của các loại đối tượng giao diện người dùng được xác định bởi sự “phát triển” về khả năng công nghệ và quy trình của hệ thống. Đối với trường hợp sơ đồ tổng quát đảm bảo về mặt công nghệ loại bỏ mọi loại thông tin không chắc chắn, các đối tượng đó là:

- từ điển đồng nghĩa cung cấp định hướng cho người dùng trong lĩnh vực chủ đề;
- từ điển hệ thống tìm kiếm được sử dụng để hình thành biểu thức tìm kiếm;
- từ điển chuyên đề đại diện cho từ vựng thông tin của lĩnh vực chủ đề.
Những đối tượng này, mang tính chất hỗ trợ về mặt công nghệ, được sử dụng ở các giai đoạn tìm kiếm khác nhau và cung cấp khả năng thể hiện ít nhiều đầy đủ nhu cầu thông tin của người dùng. Đồng thời, để phản ánh các đặc điểm riêng của IP, chúng, với tư cách là đối tượng giao diện, không thể được sử dụng một cách hiệu quả, vì do tính chất trung bình của chúng, chúng đại diện cho toàn bộ SbA.

---

Для этого на промежуточном интерфейсном уровне можно использовать иерархически организованные структуры, отражающие пользовательское видение системы понятий предметной области. Причем, каждый такой объект представляет как общепринятое, так и индивидуальное видение ПрО. Интегральность такого представления достигается за счет того, что оно реализуется объектами как уровня ресурсов (подборками документов, ссылками на ассоциированные ресурсы и т. д.), так и уровня терминологии (тезаурусами, рубрикаторами, словниками).

Để thực hiện điều này, ở cấp độ giao diện trung gian, bạn có thể sử dụng các cấu trúc được tổ chức theo thứ bậc phản ánh tầm nhìn của người dùng về hệ thống khái niệm của lĩnh vực chủ đề. Hơn nữa, mỗi đối tượng như vậy đại diện cho cả tầm nhìn được chấp nhận chung và tầm nhìn riêng của SbA. Tính toàn vẹn của cách trình bày như vậy đạt được do thực tế là nó được triển khai bởi các đối tượng ở cả cấp độ tài nguyên (bộ sưu tập tài liệu, liên kết đến các tài nguyên liên quan, v.v.) và cấp độ thuật ngữ (từ điển đồng nghĩa, bảng đánh giá, từ điển).

---

При таком подходе ИС может помимо стандартных и расширенных поисковых возможностей иметь средства систематизации информационных массивов, формирования и развития компонентов лингвистического обеспечения, а также оценки и анализа результатов поиска.

Với cách tiếp cận này, một hệ thống thông tin, ngoài khả năng tìm kiếm tiêu chuẩn và nâng cao, còn có các phương tiện để hệ thống hóa các mảng thông tin, hình thành và phát triển các thành phần hỗ trợ ngôn ngữ, cũng như đánh giá và phân tích kết quả tìm kiếm.

---

Такими объектами могут быть словари поисковой системы, тематические словники, тезаурусы, представляющие информативную лексику предметной области. Эти объекты, являясь технологически вспомогательными, используются на разных этапах поиска и обеспечивают возможность более или менее адекватного выражения информационной потребности пользователя. Однако эффективность их использования для отражения индивидуальных особенностей ИП достаточно низка, поскольку, вследствие усредненной природы, представляют предметную область в целом.

Những đối tượng như vậy có thể là từ điển công cụ tìm kiếm, từ điển chủ đề, từ điển đồng nghĩa, đại diện cho từ vựng mang tính thông tin của lĩnh vực chủ đề. Những đối tượng này, mang tính chất hỗ trợ về mặt công nghệ, được sử dụng ở các giai đoạn tìm kiếm khác nhau và cung cấp khả năng thể hiện ít nhiều đầy đủ nhu cầu thông tin của người dùng. Tuy nhiên, hiệu quả của việc sử dụng chúng để phản ánh đặc điểm cá nhân của từng doanh nhân là khá thấp, vì do tính chất trung bình nên chúng đại diện cho toàn bộ lĩnh vực chủ đề.

---

Для этого на интерфейсном уровне можно использовать иерархически организованные структуры, динамически создаваемые пользователем, отражающие его персональное видение предметной области. Причем, каждый такой объект представляет как общепринятое, так и индивидуальное видение ПрО. Интегральность такого представления достигается за счет того, что оно реализуется объектами как уровня ресурсов (подборками документов, ссылками на ассоциированные ресурсы и т. д.), так и уровня терминологии (тезаурусами, рубрикаторами, словниками).

Để thực hiện điều này, ở cấp độ giao diện, bạn có thể sử dụng các cấu trúc được tổ chức theo thứ bậc do người dùng tạo động, phản ánh tầm nhìn cá nhân của họ về lĩnh vực chủ đề. Hơn nữa, mỗi đối tượng như vậy đại diện cho cả tầm nhìn được chấp nhận chung và tầm nhìn riêng của SbA. Tính toàn vẹn của cách trình bày như vậy đạt được do thực tế là nó được triển khai bởi các đối tượng ở cả cấp độ tài nguyên (bộ sưu tập tài liệu, liên kết đến các tài nguyên liên quan, v.v.) và cấp độ thuật ngữ (từ điển đồng nghĩa, bảng đánh giá, từ điển).

### 6.4.3. Технологии отбора документов и обработки результатов

Так же, как и методы поиска, технологии, используемые в АИС, необходимо рассматривать, с одной стороны, в контексте этапности обработки запроса, и с другой – как управляемый пользователем процесс получения и преобразования операционных объектов в среде конкретного программно-технологического комплекса.

Cũng giống như các phương pháp tìm kiếm, các công nghệ được sử dụng trong AIS một mặt phải được xem xét trong bối cảnh các giai đoạn xử lý yêu cầu và mặt khác, như một quy trình do người dùng kiểm soát để thu thập và chuyển đổi các đối tượng hoạt động trong môi trường. của một phức hợp phần mềm và công nghệ cụ thể.

#### 6.4.3.1. Технологии отбора документов

Технологии формирования выдачи документов по отдельному ПОЗ, объединяют два процесса:

- процесс объявления (выражения, обозначения) пользователем информацион-ной потребности;
- процесс построения выдачи – множества документов, генерируемых системой в ответ на поисковое требование пользователя.

Công nghệ tạo ra việc phát hành tài liệu cho một PPO riêng biệt kết hợp hai quy trình:

- quá trình khai báo (biểu hiện, chỉ định) của người sử dụng thông tin có nhu cầu;
- quy trình xây dựng kết quả tìm kiếm – một bộ tài liệu do hệ thống tạo ra để đáp ứng yêu cầu tìm kiếm của người dùng.

---

Технология генерации выдачи полностью определяется рассмотренной во второй главе обобщенной архитектурой АИПС.

Công nghệ tạo đầu ra hoàn toàn được xác định bởi kiến ​​trúc AIPS tổng quát đã thảo luận trong chương thứ hai.

---

В этом смысле выделяются два класса систем: диалоговые и пакетные. В первом случае технология ориентирована на работу в реальном масштабе времени, а условие отбора по одному запросу соотносится со всеми поисковыми образами документов (ес-ли БД не имеет инвертированных массивов, являющихся избыточными по отношению к основному). При пакетной обработке запросов, предназначенной для использования в системе избирательного распределения информации, каждый поисковый образ доку-мента (чаще всего при поступлении в систему) соотносится с поисковыми образами всех запросов.

Theo nghĩa này, hai loại hệ thống được phân biệt: hộp thoại và bó. Trong trường hợp đầu tiên, công nghệ tập trung vào hoạt động trong thời gian thực và điều kiện lựa chọn cho một yêu cầu tương quan với tất cả hình ảnh tìm kiếm của tài liệu (nếu cơ sở dữ liệu không có mảng đảo ngược dư thừa so với mảng chính). Với việc xử lý hàng loạt các yêu cầu, nhằm mục đích sử dụng trong hệ thống phân phối thông tin có chọn lọc, mỗi hình ảnh tìm kiếm của một tài liệu (thường là khi vào hệ thống) sẽ tương quan với hình ảnh tìm kiếm của tất cả các yêu cầu.

---

Разнообразие технологий подготовки запроса, таким образом, в основном отно-сится к диалоговым системам, обеспечивая (в той или иной степени) не только эффек-тивность вхождения в базу, но и качество поиска в целом.

Do đó, sự đa dạng của các công nghệ chuẩn bị truy vấn chủ yếu liên quan đến hệ thống đối thoại, đảm bảo (ở mức độ này hay mức độ khác) không chỉ hiệu quả của việc nhập cơ sở dữ liệu mà còn cả chất lượng của toàn bộ tìm kiếm.

---

В контексте понятия «выражение запроса», как главного (основного) операцион-ного объекта, можно определить три типа не взаимоисключающих технологии его спе-цификации:

- непосредственного набора булевоподобного выражения;
- формирования булевоподобного выражения с помощью «конструктора запро-сов», облегчающего использование словарей, имен полей и операторов струк-турно-логической связи;
- форматно-ориентированных форм генерации «запроса по образцу».

Trong bối cảnh khái niệm “biểu thức truy vấn”, với tư cách là đối tượng hoạt động chính (chính), có thể xác định ba loại công nghệ không loại trừ lẫn nhau cho đặc tả của nó:

- gõ trực tiếp một biểu thức giống Boolean;
- hình thành một biểu thức giống Boolean bằng cách sử dụng “hàm tạo truy vấn” tạo điều kiện thuận lợi cho việc sử dụng từ điển, tên trường và toán tử kết nối logic-cấu trúc;
- các hình thức định hướng định dạng để tạo ra một “truy vấn theo mẫu”.

#### 6.4.3.2. Технологии обработки результатов поиска

Возможности АИПС по обработке результатов поиска можно рассматривать в следующих аспектах:

- управление формой представления документов и списков документов (опера-тивное изменение формата и наполнения, фрагментирование);
- управление последовательностью выдачи (сортировка, ранжирование, опера-тивные переходы с возвратами, «закладки»);
- локализация результата на уровне отдельного документа или совокупности (отметка степени соответствия информационной потребности);
- использование фрагмента документа, ссылки на документ или совокупность документов в последующих запросах, а также для развития процесса поиска;
- использование результатов поиска для оценки качества поиска.

Khả năng của AIPS để xử lý kết quả tìm kiếm có thể được xem xét ở các khía cạnh sau:

- quản lý hình thức trình bày tài liệu và danh mục tài liệu (thay đổi nhanh chóng về định dạng và nội dung, phân mảnh);
- kiểm soát trình tự phát hành (sắp xếp, xếp hạng, chuyển đổi nhanh chóng với kết quả trả về, “đánh dấu”);
- bản địa hóa kết quả ở cấp độ của một tài liệu hoặc bộ tài liệu riêng lẻ (đánh dấu mức độ tuân thủ nhu cầu thông tin);
- sử dụng một đoạn tài liệu, liên kết đến một tài liệu hoặc một bộ tài liệu trong các truy vấn tiếp theo, cũng như để phát triển quá trình tìm kiếm;
- Sử dụng kết quả tìm kiếm để đánh giá chất lượng tìm kiếm.

---

Развитые средства обработки результатов поиска предопределяют возможность разработки средств и технологий автоматической или автоматизированной реформули-ровки запроса.

Các công cụ được phát triển để xử lý kết quả tìm kiếm xác định trước khả năng phát triển các công cụ và công nghệ để định dạng lại truy vấn tự động hoặc tự động.

---

Методы ранжирования документов в выдаче основываются на использовании количественных мер, отражающих либо статистику встречаемости и взаимосвязи тер-минов в документах, либо статистику взаимосвязи документа с другими документами в выборке или в предметной области.

Các phương pháp xếp hạng tài liệu trong kết quả tìm kiếm dựa trên việc sử dụng các biện pháp định lượng phản ánh số liệu thống kê về sự xuất hiện và mối quan hệ của các thuật ngữ trong tài liệu hoặc thống kê về mối quan hệ của tài liệu với các tài liệu khác trong mẫu hoặc trong lĩnh vực chủ đề.

#### 6.4.3.3. Технологии управления поиском

Управление процессом поиска для диалоговых АИПС определяется:

- разнообразием операционных объектов и средств их обработки, определяю-щих возможные методы получения результата и особенности его представле-ния;
- интерфейсными решениями (зависящими от архитектуры программно-технического комплекса), определяющими степень гибкости сценария и его управляемость как пользователем, так и системой.

Việc kiểm soát quá trình tìm kiếm AIPS tương tác được xác định bởi:

- nhiều đối tượng hoạt động và phương tiện xử lý chúng, xác định các phương pháp có thể để đạt được kết quả và các đặc điểm của việc trình bày nó;
- giải pháp giao diện (tùy thuộc vào kiến ​​trúc của phần mềm và phần cứng phức tạp), xác định mức độ linh hoạt của kịch bản và khả năng kiểm soát của cả người dùng và hệ thống.

---

Рассматривая поиск в контексте понятия «стратегия» и представляя его как ди-намический процесс с изменяющимися состояниями сторон диалога (пользователь – система), можно (хотя и очень условно) выделить три типа поисковых технологий:

- «запрос-ответ», как реализацию истинно вербальной стратегии;
- «накопления результата», когда система позволяет не только использовать ссылки на результаты отдельных поисков, но и получать сам результат спосо-бом, отличным от запросно-ответного;
- «распространяющейся активности», позволяющую не только изменять способ получения результата, но и изменять цель – предмет поиска, обеспечивая как дифференцированное использование результатов, так и восстановление поис-ковой ситуации.

Xem xét tìm kiếm trong bối cảnh khái niệm “chiến lược” và trình bày nó như một quá trình năng động với các trạng thái thay đổi của các bên tham gia đối thoại (người dùng - hệ thống), có thể phân biệt ba loại công nghệ tìm kiếm (mặc dù rất có điều kiện):

- “yêu cầu-phản hồi” là việc thực hiện một chiến lược bằng lời nói thực sự;
- “tích lũy kết quả”, khi hệ thống không chỉ cho phép sử dụng các liên kết đến kết quả của từng tìm kiếm riêng lẻ mà còn có thể lấy chính kết quả đó theo cách khác với phương pháp phản hồi yêu cầu;
- “hoạt động lan truyền”, cho phép không chỉ thay đổi phương pháp thu được kết quả mà còn thay đổi mục tiêu - chủ đề tìm kiếm, cung cấp cả cách sử dụng kết quả một cách khác biệt và khôi phục tình hình tìm kiếm.

Таблица 6.3. Средства, технологии и механизмы поиска

| Механизм поиска | Стартовый объект | Лексическая основа для реформулировки запроса | Технология поиска | Постобработка выдачи | Интерфейсные средства управления |
| --- | --- | --- | --- | --- | --- |
| Поиск по терминам, выделенным в документе | Отдельный просматриваемый документ | Термины, выделенные пользователем | Булев поиск по всем текстовым полям с автоматической нормализацией терминов | Нет | Нет |
| Поиск «аналогов» | Отдельный просматриваемый документ | Содержание просматриваемого документа | Нечеткий поиск: по условию частичного вхождения с указанным порогом | Ранжирование по суммарному числу вхождений поисковых терминов | Диалоговая панель
«Поиск аналогов» |
| Эвристический поиск | Множество документов предложения запроса из протокола | Термины всех поисковых полей из документов, отмеченных как релевантные (словника не предъявляемого пользователю) | Поиск по статистически наиболее значимым кластерам терминов из словника | В соответствии с порядком ранжирования кластеров | Нет |
| Контекстный поиск | Множество документов предложения запроса из протокола | Отмеченные термины словника, создаваемого системой из всех поисковых полей документов, отмеченных как релевантные | Поиск по кластерам терминов из словника, отмеченных как релевантные | В соответствии с порядком ранжирования кластеров | 1. Словник. 2. Предложения протокола, содержащие результат поиска по каждому кластеру терминов |

---

Естественное представление результатов поиска как множества документов также имеет свои особенности, связанные с постобработкой результата в циклическом поисковом процессе.

Cách biểu diễn tự nhiên của kết quả tìm kiếm dưới dạng một tập hợp tài liệu cũng có những đặc điểm riêng liên quan đến việc xử lý hậu kỳ kết quả trong quy trình tìm kiếm theo chu kỳ.

Во-первых, реализация отдельных механизмов поиска (поиск по совпадению терминов, поиск аналогов, поиск «похожих» документов, поиск с использованием об-ратной связи по релевантности) требует обязательного ранжирования выдачи (а иногда и усечения), так как применение этих механизмов приводит к выдачам большого объе-ма. В этом случае средства представления и постобработки результата ориентируются на формальные методы ранжирования (в соответствии с конкретным механизмом поис-ка).

Thứ nhất, việc triển khai các cơ chế tìm kiếm riêng lẻ (tìm kiếm theo các thuật ngữ phù hợp, tìm kiếm từ tương tự, tìm kiếm các tài liệu “tương tự”, tìm kiếm bằng cách sử dụng phản hồi liên quan) yêu cầu xếp hạng bắt buộc các kết quả (và đôi khi cắt bớt), vì việc sử dụng các cơ chế này dẫn đến cho các vấn đề có khối lượng lớn. Trong trường hợp này, các phương tiện trình bày và xử lý hậu kỳ kết quả được hướng tới các phương pháp xếp hạng chính thức (theo cơ chế tìm kiếm cụ thể).

---

Во-вторых, для инициации новых поисковых циклов могут использоваться до-кументы, полученные на очередном этапе поискового процесса. Использование лекси-ки документа для формирования ПОЗ происходит либо путем альтернативного цвето-вого выделения самих терминов внутри документа, либо путем формирования количе-ственного запроса – требования на поиск документов, имеющих заявленное количество любых общих терминов с текущим. Здесь средства представления результата должны учитывать возможную постобработку, которая носит управляющий характер: материал каждого документа должен быть доступен для составления запроса и запуска поисково-го механизма.

Thứ hai, các tài liệu thu được ở giai đoạn tiếp theo của quá trình tìm kiếm có thể được sử dụng để bắt đầu các chu trình tìm kiếm mới. Việc sử dụng từ vựng tài liệu để tạo POS xảy ra bằng cách đánh dấu màu thay thế của chính các thuật ngữ trong tài liệu hoặc bằng cách tạo truy vấn định lượng - yêu cầu tìm kiếm các tài liệu có số lượng đã nêu của bất kỳ thuật ngữ phổ biến nào với thuật ngữ hiện tại. Ở đây, phương tiện trình bày kết quả phải tính đến khả năng xử lý hậu kỳ, có tính chất kiểm soát: tài liệu của mỗi tài liệu phải có sẵn để soạn truy vấn và khởi chạy công cụ tìm kiếm.

---

И, наконец, в-третьих, каждый очередной этап поискового цикла должен в идеа-ле пополнять для пользователя коллекцию документов, формируя тем самым персо-нальную тематическую область. Это означает, что все полученные пользователем результаты должны быть ему доступны, по крайней мере, как множество документов. Эту задачу решает для пользователя такое средство представления результатов, как прото-кол поиска. Назначение такой метаинформационной структуры в первую очередь в том, чтобы предоставить (через лексику запроса) доступ к каждому из документов любого промежуточного результата (при этом протокол хранит и способ получения отдельного результата). Таким образом, ПОЗ становятся такими же элементами для составления запроса, как и термины частотного словаря, что делает возможным использование при очередном цикле поиска ранее полученных результатов.

Và cuối cùng, thứ ba, mỗi giai đoạn tiếp theo của chu trình tìm kiếm lý tưởng nhất là nên bổ sung bộ sưu tập tài liệu cho người dùng, từ đó hình thành một khu vực chuyên đề cá nhân. Điều này có nghĩa là tất cả các kết quả mà người dùng thu được phải có sẵn cho anh ta, ít nhất là dưới dạng một bộ tài liệu. Vấn đề này được giải quyết cho người dùng bằng phương tiện trình bày kết quả, chẳng hạn như giao thức tìm kiếm. Mục đích của cấu trúc siêu thông tin như vậy chủ yếu là cung cấp quyền truy cập (thông qua từ vựng truy vấn) vào từng tài liệu của bất kỳ kết quả trung gian nào (đồng thời, giao thức cũng lưu trữ phương thức để thu được một kết quả riêng biệt). Do đó, POS trở thành các thành phần tương tự để soạn câu truy vấn giống như các thuật ngữ của từ điển tần số, điều này cho phép sử dụng các kết quả thu được trước đó trong chu kỳ tìm kiếm tiếp theo.

---

Общая характеристика средств, технологий и механизмов поиска приведена в табл. 6.3. При этом рассмотренная схема поиска отражает следующие требования к интерфейсным компонентам и организации процесса поиска в целом:

- подготовка следующего шага поиска выполняется непосредственно при обра-ботке результата предыдущего: для развития поиска в качестве основного ин-терфейсного объекта в первую очередь используются документы;
- операционные объекты однородны на каждом шаге;
- на каждом шаге возможен возврат к ранее полученным результатам или опе-ративное переключение на другую тему и операцию;
- оценка степени завершенности (сходимости) процесса поиска возможна по критерию исчерпания как лексики, так и документального пространства темы.

Đặc điểm chung của các công cụ, công nghệ và cơ chế tìm kiếm được đưa ra trong Bảng. 6.3. Đồng thời, sơ đồ tìm kiếm được xem xét phản ánh các yêu cầu sau đối với các thành phần giao diện và tổ chức toàn bộ quá trình tìm kiếm:

- việc chuẩn bị cho bước tìm kiếm tiếp theo được thực hiện trực tiếp khi xử lý kết quả của bước trước đó: để phát triển tìm kiếm, tài liệu chủ yếu được sử dụng làm đối tượng giao diện chính;
- đối tượng vận hành đồng nhất ở mỗi bước;
- ở mỗi bước có thể quay lại kết quả thu được trước đó hoặc nhanh chóng chuyển sang chủ đề và thao tác khác;
- Có thể đánh giá mức độ đầy đủ (hội tụ) của quá trình tìm kiếm dựa trên tiêu chí cạn kiệt cả từ vựng và không gian tài liệu của chủ đề.

---

Тем самым, классическая схема выдачи документов «по запросу-выражению» расширена до динамически управляемого процесса построения систематизированного пространства документов и терминов. При этом процесс поиска построен симметрично и реализует двойственную задачу: при подготовке запроса можно формировать коллекцию документов, а при формировании поисковой выдачи – реформулировать запрос и формировать компоненты лингвистического обеспечения.

Do đó, sơ đồ cổ điển để phát hành tài liệu “theo biểu thức yêu cầu” được mở rộng thành một quy trình được kiểm soát linh hoạt nhằm xây dựng một không gian tài liệu và thuật ngữ được hệ thống hóa. Đồng thời, quá trình tìm kiếm được xây dựng đối xứng và thực hiện một nhiệm vụ kép: khi chuẩn bị yêu cầu, bạn có thể hình thành một tập hợp tài liệu và khi tạo kết quả tìm kiếm, bạn có thể định dạng lại yêu cầu và các thành phần biểu mẫu hỗ trợ ngôn ngữ.

## Контрольные вопросы

1. Определите основные информационные объекты и преобразования в схеме воспроизводства информации.
2. Охарактеризуйте технологические составляющие информационного поиска.
3. Приведите типологию поисковых задач и их примеры для каждого типа.
4. Охарактеризуйте типы информационной неопределенности при поиске.
5. Определите условия установления соответствия информационной потребности и содержания документа БД.
6. Проведите сравнительный анализ понятий поисковая стратегия и поисковая навигация.
7. Охарактеризуйте основные этапы процесса информационного поиска.
8. Перечислите основные и технологические объекты, используемые при поиске.
9. Перечислите интерфейсные объекты, используемые для реализации технологии «обратной связи» в процессе информационного поиска.
10. Проведите сравнительный анализ вербальной и кластерной стратегий поиска.
11. Определите зависимость методов построения запроса и стратегий поиска.

---

1. Xác định các đối tượng thông tin chính và các biến đổi trong sơ đồ tái tạo thông tin.
2. Mô tả các thành phần công nghệ truy xuất thông tin.
3. Đưa ra các loại nhiệm vụ tìm kiếm và ví dụ cho từng loại.
4. Mô tả các loại thông tin không chắc chắn trong quá trình tìm kiếm.
5. Xác định điều kiện thiết lập sự phù hợp giữa nhu cầu thông tin và nội dung tài liệu cơ sở dữ liệu.
6. Tiến hành phân tích so sánh chiến lược tìm kiếm khái niệm và điều hướng tìm kiếm.
7. Mô tả các giai đoạn chính của quá trình tìm kiếm thông tin.
8. Liệt kê các đối tượng chính và công nghệ được sử dụng trong tìm kiếm.
9. Liệt kê các đối tượng giao diện dùng để triển khai công nghệ phản hồi trong quá trình truy xuất thông tin.
10. Tiến hành phân tích so sánh các chiến lược tìm kiếm bằng lời nói và cụm từ.
11. Xác định mối liên hệ giữa phương pháp xây dựng truy vấn và chiến lược tìm kiếm.