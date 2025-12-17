# Lộ Trình AI Engineer Full-Stack

Theo dõi chi tiết từng ngày: Lý thuyết, Thực hành & Dự án

## Giai đoạn 1: Toán – Python – Tư duy lập trình

**Thời gian:** 6 Tuần | Tập trung 80% Thực hành
**Mục tiêu:** Nắm vững Python, tư duy thuật toán và toán học nền tảng cho AI (Vector, Ma trận).
**Công cụ:** VS Code, Git, Python 3.x

### Tuần 1: Python Cơ Bản & Setup

_Viết được script chạy logic cơ bản, quản lý code bằng Git._

#### Ngày 1

- ✅ **LEARN**: Cài đặt VS Code, Python, Git. Biến (int, float, str), Kiểu dữ liệu.
- ✅ **CODE**: Viết chương trình tính chỉ số BMI, đổi nhiệt độ C sang F.

#### Ngày 2

- ✅ **LEARN**: Câu lệnh điều kiện (if-else), Vòng lặp (for, while).
- ✅ **CODE**: Giải phương trình bậc 2. Game đoán số (Random number guessing).

#### Ngày 3

- ✅ **LEARN**: List, Tuple, Set. Các method xử lý List.
- ✅ **CODE**: Tìm số lớn nhất, sắp xếp list, xóa phần tử trùng lặp.

#### Ngày 4

- ✅ **LEARN**: Dictionary (Từ điển) - Cấu trúc quan trọng nhất.
- ✅ **CODE**: Tạo từ điển Anh-Việt. Đếm số lần xuất hiện từ trong đoạn văn.

#### Ngày 5

- ✅ **LEARN**: Hàm (Function), Tham số, Return.
- ✅ **CODE**: Refactor bài tập tuần trước thành các hàm riêng biệt.

#### Ngày 6

- ✅ **LEARN**: Git cơ bản: git init, add, commit, push.
- ✅ **CODE**: Tạo repo GitHub và đẩy toàn bộ bài tập tuần này lên.

### Tuần 2: Python Nâng cao & DSA

_Hiểu cách xử lý dữ liệu phức tạp và tối ưu code._

#### Ngày 7

- ✅ **LEARN**: List Comprehension, Lambda functions.
- ✅ **CODE**: Viết lại các vòng lặp xử lý list chỉ bằng 1 dòng code.

#### Ngày 8

- ✅ **LEARN**: Xử lý chuỗi nâng cao: split, join, strip, replace.
- ✅ **CODE**: Bài tập chuẩn hóa tên người dùng (viết hoa, xóa khoảng trắng).

#### Ngày 9

- ✅ **LEARN**: File Handling (Đọc/Ghi file .txt).
- ✅ **CODE**: Đọc file log và lọc các dòng báo lỗi 'ERROR'.

#### Ngày 10

- ✅ **LEARN**: Môi trường ảo (Virtual Environments)
- ✅ **CODE**: Dùng venv làm Tool Web, Dùng conda giả lập môi trường cũ

#### Ngày 11

- ✅ **LEARN**: Python Package Manager (Pip & Conda)
- ✅ **CODE**: Bài tập 1 (Terminal): Tạo môi trường ảo mới bằng conda (Python 3.9). Cài đặt thư viện pandas và matplotlib. Xuất danh sách thư viện ra file environment.yml (chuẩn Conda) hoặc requirements.txt (chuẩn Pip).
- ✅ **CODE**: Bài tập 2 (Simulation): Xóa môi trường vừa tạo. Dùng lệnh để khôi phục lại toàn bộ môi trường chỉ từ file cấu hình vừa xuất.

#### Ngày 12

- ✅ **LEARN**: Python Type Errors - Các lỗi phổ biến trong Python
- ✅ **CODE**: Bài tập (Bug Hunting): Chạy code để xem Python báo lỗi gì (IndexError, KeyError, TypeError, IndentationError, NameError). Giải thích tại sao lỗi. Sửa lại cho chạy đúng.

#### Ngày 13

- ✅ **LEARN**: Exception Handling (Try-Except)
- ✅ **CODE**: Máy tính an toàn, truy xuất dữ liệu an toàn

#### Ngày 14

- ✅ **LEARN**: Regular Expressions (Regex)
- ✅ **CODE**: Trích xuất Email & SĐT, Làm sạch Password

### Tuần 3: Python Hướng đối tượng (OOP) & Advanced

_Chuyển tư duy từ viết hàm rời rạc sang kiến trúc Class (rất quan trọng cho PyTorch sau này)._

#### Ngày 15

- ✅ **LEARN**: OOP Basic: Class & Object: Hiểu Class, Object, self, Hàm **init** constructor
- ✅ **CODE**: Tạo class Student với các thuộc tính name, age, grades

#### Ngày 16

- ✅ **LEARN**: OOP: Inheritance (Kế thừa) & Polymorphism: Tạo class con kế thừa class cha, Override phương thức
- ✅ **CODE**: Tạo class AI_Student kế thừa Student, thêm thuộc tính 'specialization'

#### Ngày 17

- ✅ **LEARN**: OOP: Encapsulation (Đóng gói): Private variables (\_\_var), Getter & Setter methods
- ✅ **CODE**: Bảo mật điểm số sinh viên, chỉ cho sửa qua hàm setter có validation
- ✅ **LEARN**: Trừu tượng (Abstraction) & Đa hình (Polymorphism)
- ✅ **CODE**: "Sở thú AI" (AI Model Zoo)

#### Ngày 18

- 📘 **LEARN**: Python Advanced: Decorators: Hiểu First-class functions,Higher-order Function, Viết Wrapper function, decorator
- 💻 **CODE**: Higher-Order Function(Bước đệm),Wrapper Function (Cơ chế lõi),Decorator @debug (Thử thách)
- 💻 **CODE**: Viết decorator @timer để đo thời gian chạy của một hàm (Quan trọng để tối ưu code AI)

#### Ngày 19

- 📘 **LEARN**: Python Advanced: Generators & Iterators: yield keyword vs return, Xử lý dữ liệu lớn bằng Generator
- 💻 **CODE**: Viết hàm sinh số Fibonacci vô hạn bằng yield

#### Ngày 20

- 📘 **LEARN**: Exception Handling & Modules: try-except-finally custom, Tổ chức code thành modules/packages
- 💻 **CODE**: Nâng cấp bài Student Manager: Xử lý lỗi nhập liệu, tách file main.py và student.py

#### Ngày 21

- 📘 **LEARN**: Review & Project OOP
- 💻 **CODE**: Project: Upgrade CLI Student Manager. Chuyển toàn bộ code ngày 1-10 sang dạng Class. Lưu data vào JSON bằng method của Class.

### Tuần 4: Đại số tuyến tính (Linear Algebra) & Code Ma trận

_Hiểu cách máy tính nhìn dữ liệu (dưới dạng Vector và Matrix)._

#### Ngày 22

- 📘 **LEARN**: Scalar, Vector & Matrix: Khái niệm không gian vector, Biểu diễn ảnh dưới dạng ma trận
- 💻 **CODE**: Dùng Python List of Lists để biểu diễn Ma trận 2x2, 3x3

#### Ngày 23

- 📘 **LEARN**: Các phép toán trên Ma trận (Cộng, Trừ, Scalar Multiply): Element-wise operations
- 💻 **CODE**: Viết hàm matrix_add(A, B) và matrix_scalar_mul(A, k) không dùng thư viện

#### Ngày 24

- 📘 **LEARN**: Dot Product (Tích vô hướng) - QUAN TRỌNG NHẤT: Công thức nhân dòng x cột, Ý nghĩa hình học (góc giữa 2 vector)
- 📘 **LEARN**: Norm (L1/L2), Distance & Cosine Similarity: liên hệ với Dot Product và ứng dụng trong similarity/search.
- 💻 **CODE**: Viết hàm dot_product(v1, v2) thủ công

#### Ngày 25

- 📘 **LEARN**: Matrix Multiplication (Nhân ma trận): Điều kiện nhân (mxn \* nxp), Độ phức tạp tính toán
- 💻 **CODE**: Viết hàm matrix_multiply(A, B) sử dụng 3 vòng for lồng nhau

#### Ngày 26

- 📘 **LEARN**: Transposition (Chuyển vị) & Reshape: Ma trận chuyển vị A.T, Thay đổi hình dạng ma trận (Flatten)
- 📘 **LEARN**: Vector Space, Basis & Orthonormal; Projection (chiếu vector) – trực giác dùng trong least squares/PCA.
- 💻 **CODE**: Viết hàm transpose(matrix)

#### Ngày 27

- 📘 **LEARN**: Broadcasting (Khái niệm): Cách NumPy cộng 1 vector vào 1 ma trận (lý thuyết trước khi dùng thư viện)
- 📘 **LEARN**: Eigenvalues/Eigenvectors (trực giác): vì sao 'hướng riêng' quan trọng trong ổn định, PCA, và dynamics của gradient.
- 💻 **CODE**: Mô phỏng broadcasting bằng Python thuần

#### Ngày 28

- 📘 **LEARN**: Project: Mini Numpy Part 1
- 📘 **LEARN**: SVD & PCA (trực giác): giảm chiều, nén thông tin; liên hệ embeddings và curse of dimensionality.
- 💻 **CODE**: Project: MyLinearAlgebra Library. Gói các hàm dot, multiply, transpose vào Class 'MyMatrix'. Test với dữ liệu mẫu.

### Tuần 5: Giải tích (Calculus) & Xác suất cơ bản

_Hiểu Gradient Descent hoạt động thế nào (Đạo hàm)._

#### Ngày 29

- 📘 **LEARN**: Đạo hàm (Derivative) cơ bản: Tốc độ thay đổi tức thời, Quy tắc chuỗi (Chain rule - Cốt lõi của Backpropagation)
- 💻 **CODE**: Viết hàm tính đạo hàm x^2 tại điểm x=3 (numerical differentiation)

#### Ngày 30

- 📘 **LEARN**: Gradient & Partial Derivative (Đạo hàm riêng): Gradient là vector các đạo hàm riêng, Ý nghĩa trong tìm cực tiểu hàm số
- 💻 **CODE**: Mô phỏng thuật toán Gradient Descent tìm điểm cực tiểu của y = x^2 - 4x

#### Ngày 31

- 📘 **LEARN**: Thống kê mô tả (Descriptive Stats): Mean (Trung bình), Median (Trung vị), Mode
- 📘 **LEARN**: Expectation, Variance, Covariance/Correlation: cách đọc tương quan, phân biệt correlation vs causation.
- 💻 **CODE**: Viết hàm calculate_mean(data), calculate_median(data)

#### Ngày 32

- 📘 **LEARN**: Variance & Standard Deviation (Phương sai & Độ lệch chuẩn): Đo độ phân tán của dữ liệu, Tại sao chia cho N hay N-1
- 📘 **LEARN**: Sampling, Standard Error & Confidence Interval (CI): trực giác 'độ chắc chắn' khi ước lượng từ mẫu.
- 💻 **CODE**: Viết hàm calculate_std(data) từ con số 0

#### Ngày 33

- 📘 **LEARN**: Probability Distributions (Phân phối xác suất): Phân phối chuẩn (Gaussian/Normal Distribution), Hàm mật độ xác suất
- 📘 **LEARN**: Conditional Probability & Bayes Theorem; các phân phối hay gặp: Bernoulli/Binomial/Poisson/Exponential (ý nghĩa + khi nào dùng).
- 💻 **CODE**: Dùng random.gauss() để sinh dữ liệu giả lập chiều cao con người

#### Ngày 34

- 📘 **LEARN**: Softmax & Sigmoid Functions: Hàm kích hoạt (Activation function), Công thức Softmax chuyển đổi ra xác suất
- 💻 **CODE**: Viết hàm sigmoid(x) và softmax(list_x)

#### Ngày 35

- 📘 **LEARN**: Project: Mini Numpy Part 2
- 📘 **LEARN**: Hypothesis Testing & p-value (trực giác, không sa đà công thức); A/B testing: power, sample size, tránh kết luận sai.
- 💻 **CODE**: Project: MyStats Library. Thêm các hàm mean, std, softmax vào thư viện Mini Numpy. Đóng gói thành module hoàn chỉnh.

### Tuần 6: Data Structures & Algorithms (DSA) - Basic

_Viết code tối ưu hơn, chuẩn bị cho phỏng vấn._

#### Ngày 36

- 📘 **LEARN**: Độ phức tạp thuật toán (Big O Notation): O(1), O(n), O(n^2), Tại sao tránh vòng lặp lồng nhau
- 💻 **CODE**: So sánh thời gian chạy hàm tìm kiếm O(n) vs O(1) (Dict lookup)

#### Ngày 37

- 📘 **LEARN**: Array & String Manipulation (Nâng cao): Two Pointers technique, Sliding Window
- 💻 **CODE**: LeetCode bài Two Sum (phiên bản tối ưu)

#### Ngày 38

- 📘 **LEARN**: Hash Map / Dictionary (Deep Dive): Xử lý đụng độ (Collision), Khi nào dùng Hash Map
- 💻 **CODE**: Giải bài toán đếm tần suất xuất hiện ký tự (dùng Dict)

#### Ngày 39

- 📘 **LEARN**: Stack & Queue: LIFO (Last In First Out), FIFO (First In First Out)
- 💻 **CODE**: Implement Stack bằng List

#### Ngày 40

- 📘 **LEARN**: Recursion (Đệ quy): Điều kiện dừng, Stack overflow là gì
- 💻 **CODE**: Tính giai thừa, dãy Fibonacci bằng đệ quy

#### Ngày 41

- 📘 **LEARN**: Sorting Algorithms: Bubble Sort (để biết), Quick Sort / Merge Sort (để dùng)
- 💻 **CODE**: Implement Quick Sort đơn giản

#### Ngày 42

- 📘 **LEARN**: Binary Search (Tìm kiếm nhị phân): Tìm trong danh sách đã sắp xếp O(log n)
- 💻 **CODE**: Viết hàm binary_search thủ công

### Tuần 7: Tổng hợp & Capstone Project Stage 1

#### Ngày 43

- 📘 **LEARN**: Unit Testing: Tại sao cần test, Thư viện unittest/pytest cơ bản
- 💻 **CODE**: Viết test case cho thư viện Mini Numpy đã làm

#### Ngày 44

- 📘 **LEARN**: CAPSTONE PROJECT 1: Mini Numpy from Scratch (Final): Class Matrix: hỗ trợ cộng, nhân, chuyển vị., Module Stats: tính mean, std., Module Activation: softmax, sigmoid., Viết documentation (Readme.md) cách sử dụng., Push lên GitHub với cấu trúc thư mục chuẩn.

### Tuần 8: Nghỉ ngơi & Review (Gap week)

_Ôn tập lại kiến thức 7 tuần qua, chuẩn bị sang Stage 2 (Data Science)._

#### Ngày 45

- 📘 **LEARN**: Review code cũ, đọc sách 'Grokking Algorithms' hoặc nghỉ xả hơi.

## Giai đoạn 2: Data Analysis & Feature Engineering

**Thời gian:** Tuần 9 đến Tuần 16 (8 Tuần)
**Mục tiêu:** Biến dữ liệu thô thành thông tin giá trị (Insights) và đầu vào cho Model.
**Công cụ:** Pandas, NumPy, Matplotlib/Seaborn, SQL, Scikit-learn (Preprocessing)

### Tuần 9: NumPy & Pandas Foundation (Cốt lõi)

_Thao tác thành thạo DataFrame - Cấu trúc dữ liệu quan trọng nhất ngành Data._

#### Ngày 46

- 📘 **LEARN**: NumPy to Real World: Broadcasting, Vectorization (Thay thế vòng for chậm chạp), Indexing & Slicing nâng cao
- 💻 **CODE**: Tối ưu hóa bài toán nhân ma trận Stage 1 bằng NumPy (1 dòng code).

#### Ngày 47

- 📘 **LEARN**: Pandas Series & DataFrame: Cấu trúc DataFrame, Đọc dữ liệu (read_csv, read_excel, read_json)
- 💻 **CODE**: Load file CSV 1 triệu dòng, kiểm tra .info(), .describe().

#### Ngày 48

- 📘 **LEARN**: Data Selection & Filtering: loc vs iloc, Boolean Indexing (Lọc theo điều kiện), Query method
- 💻 **CODE**: Lọc danh sách khách hàng > 30 tuổi và mua hàng > 100$.

#### Ngày 49

- 📘 **LEARN**: Data Cleaning 1: Xử lý dữ liệu lỗi: Kiểm tra null (isna), Xóa null (dropna), Điền giá trị thiếu (fillna)
- 💻 **CODE**: Xử lý dataset bị thiếu tuổi: điền bằng trung bình hoặc trung vị.

#### Ngày 50

- 📘 **LEARN**: Data Manipulation: Apply & Map: Hàm .apply() (Powerful but slow), Hàm .map(), Lambda functions trong Pandas
- 💻 **CODE**: Tạo cột mới 'AgeGroup' từ cột 'Age' dùng apply.

### Tuần 10: Advanced Pandas & Aggregation

_Trả lời các câu hỏi nghiệp vụ phức tạp (Business Questions)._

#### Ngày 51

- 📘 **LEARN**: GroupBy & Aggregation: Split-Apply-Combine strategy, Các hàm agg (sum, mean, count)
- 💻 **CODE**: Tính doanh thu trung bình theo từng thành phố và từng tháng.

#### Ngày 52

- 📘 **LEARN**: Merge & Join: Inner, Outer, Left, Right Join (Giống SQL), Concat DataFrames
- 💻 **CODE**: Ghép bảng 'Users' và bảng 'Orders' để tìm ai mua nhiều nhất.

#### Ngày 53

- 📘 **LEARN**: Pivot Tables & Crosstab: Tạo bảng tổng hợp nhiều chiều (Giống Excel Pivot), Stack/Unstack
- 💻 **CODE**: Tạo Pivot Table so sánh doanh số theo Năm (cột) và Loại hàng (dòng).

#### Ngày 54

- 📘 **LEARN**: Time Series Data (Dữ liệu thời gian): datetime objects, Resampling (gom data theo ngày/tuần/tháng), Time shifts
- 💻 **CODE**: Tính doanh thu theo từng tuần (Weekly Sales) từ data log từng giây.

#### Ngày 55

- 📘 **LEARN**: Mini Project Week 10
- 💻 **CODE**: Project: Sales Analysis. Cho file sales.csv. Hỏi: Tháng nào bán tốt nhất? Thành phố nào mua nhiều nhất? Thời điểm nào trong ngày khách hay mua?

### Tuần 11: Data Visualization & Storytelling

_Vẽ hình để tìm Insight (không phải vẽ cho đẹp)._

#### Ngày 56

- 📘 **LEARN**: Matplotlib cơ bản: Figure, Axes structure, Line, Bar, Scatter plot
- 💻 **CODE**: Vẽ biểu đồ đường doanh thu theo thời gian.

#### Ngày 57

- 📘 **LEARN**: Seaborn & Statistical Plots: Distplot (Phân phối), Boxplot (Phát hiện Outlier - Quan trọng), Violin plot
- 💻 **CODE**: Dùng Boxplot tìm xem có đơn hàng nào giá trị cao bất thường không.

#### Ngày 58

- 📘 **LEARN**: Multivariate Analysis (Phân tích đa biến): Heatmap (Ma trận tương quan - Correlation Matrix), Pairplot
- 💻 **CODE**: Vẽ Heatmap xem 'Giá nhà' tương quan thế nào với 'Diện tích' và 'Số phòng'.

#### Ngày 59

- 📘 **LEARN**: Visual Storytelling: Chọn đúng loại biểu đồ, Màu sắc, Tiêu đề, Label, Tránh biểu đồ gây hiểu lầm
- 💻 **CODE**: Refactor lại các biểu đồ cũ cho chuyên nghiệp, sẵn sàng để báo cáo.

### Tuần 12: SQL for Data Science

_Lấy dữ liệu từ Database (Kỹ năng bắt buộc khi đi làm)._

#### Ngày 60

- 📘 **LEARN**: SQL Basic Review: SELECT, FROM, WHERE, ORDER BY, LIMIT
- 💻 **CODE**: Viết query lấy Top 10 khách hàng chi tiêu cao nhất.

#### Ngày 61

- 📘 **LEARN**: Joins & Unions: INNER vs LEFT JOIN, Xử lý NULL sau khi Join
- 💻 **CODE**: Join 3 bảng: Customers, Orders, Products.

#### Ngày 62

- 📘 **LEARN**: Aggregation & Grouping: GROUP BY, HAVING (Lọc sau khi Group)
- 💻 **CODE**: Tìm các danh mục sản phẩm có tổng doanh thu > 10.000$.

#### Ngày 63

- 📘 **LEARN**: Window Functions (Nâng cao - Cực quan trọng): ROW_NUMBER(), RANK(), LEAD/LAG (So sánh dòng trước/sau)
- 💻 **CODE**: Tìm top 3 nhân viên xuất sắc nhất của TỪNG phòng ban (Partition By).

#### Ngày 64

- 📘 **LEARN**: CTEs (Common Table Expressions): WITH clause, Viết query dễ đọc hơn
- 💻 **CODE**: Viết CTE tính doanh thu tháng, sau đó query chính tính tăng trưởng so với tháng trước.

### Tuần 13: Feature Engineering (Kỹ thuật đặc trưng)

_Biến dữ liệu thô thành dữ liệu mà Model hiểu được._

#### Ngày 65

- 📘 **LEARN**: Feature Scaling (Chuẩn hóa): Normalization (Min-Max), Standardization (Z-score), Khi nào dùng cái nào?
- 💻 **CODE**: Dùng Scikit-learn StandardScaler để chuẩn hóa cột 'Salary'.

#### Ngày 66

- 📘 **LEARN**: Encoding Categorical Data (Mã hóa phân loại): One-Hot Encoding, Label Encoding, Target Encoding
- 💻 **CODE**: Chuyển cột 'Màu sắc' (Đỏ, Xanh) thành vector số học.

#### Ngày 67

- 📘 **LEARN**: Handling Outliers (Xử lý ngoại lai): IQR Method, Z-score method, Capping/Flooring
- 💻 **CODE**: Viết hàm tự động loại bỏ các giá trị ngoại lai trong Dataset.

#### Ngày 68

- 📘 **LEARN**: Feature Selection: Correlation filter, Variance threshold, Tại sao ít feature lại tốt hơn?
- 💻 **CODE**: Loại bỏ các cột có độ tương quan > 0.9 (Dư thừa).

### Tuần 14: Polars & Modern Tools (Optional but Recommended)

_Làm quen công cụ xử lý dữ liệu lớn tốc độ cao._

#### Ngày 69

- 📘 **LEARN**: Intro to Polars: Lazy Evaluation, So sánh tốc độ với Pandas
- 💻 **CODE**: Viết lại bài toán GroupBy của Pandas bằng Polars.

### Tuần 15 (Bổ sung): Big Data với Apache Spark & PySpark

_Làm quen với xử lý dữ liệu lớn phân tán bằng Apache Spark/PySpark, chuẩn bị cho các hệ thống AI quy mô doanh nghiệp._

#### Ngày 70

- 📘 **LEARN**: Giới thiệu Big Data & Apache Spark: Cluster, Driver, Executor, RDD vs DataFrame. Tại sao Spark nhanh hơn chỉ dùng Pandas?
- 💻 **CODE**: Cài đặt PySpark (local). Viết script đơn giản đọc file CSV lớn, gọi .count() và .show().

#### Ngày 71

- 📘 **LEARN**: Transformations & Actions trong Spark: select, filter, withColumn, groupBy, agg. Lazy evaluation là gì?
- 💻 **CODE**: Dùng PySpark DataFrame để tính tổng doanh thu theo ngày/tháng trên dataset > 1GB (giả lập nếu cần).

#### Ngày 72

- 📘 **LEARN**: Joins trong Spark: inner, left, right, full outer. Khi nào cần repartition/broadcast join để tối ưu?
- 💻 **CODE**: Ghép 2 bảng lớn (Users, Events) bằng PySpark, tính DAU/MAU, top 10 user có nhiều event nhất.

#### Ngày 73

- 📘 **LEARN**: Partitioning & Caching: partitionBy, coalesce, persist/cache. Đọc hiểu Spark UI và explain() để tối ưu query.
- 💻 **CODE**: So sánh thời gian chạy: cùng một pipeline ETL nhưng có/không có cache(), có/không có partition hợp lý.

#### Ngày 74

- 📘 **LEARN**: Spark trên Cloud (high-level): Databricks, EMR, GCP Dataproc. Khái niệm job, cluster size, autoscaling.
- 💻 **CODE**: Đóng gói notebook/py script ETL bằng PySpark: đọc dữ liệu raw → làm sạch → aggregate → ghi ra Parquet/Delta. Viết README mô tả pipeline.

### Tuần 16 (Bổ sung): Data Modeling, Data Quality & Lakehouse Basics

_Nắm tư duy hệ dữ liệu để xây pipeline ML/analytics bền vững: modeling, định dạng lưu trữ, chất lượng dữ liệu, versioning/lineage._

#### Ngày 75

- 📘 **LEARN**: Data Modeling 101: OLTP vs OLAP, Fact/Dimension, grain; Star schema (tư duy thiết kế bảng).
- 💻 **CODE**: Chọn 1 dataset (e-commerce) và phác thảo star schema: dim_date, dim_user, dim_product, fact_orders (viết markdown + tạo dataframe mẫu).

#### Ngày 76

- 📘 **LEARN**: File Formats & Storage: CSV vs Parquet; row vs columnar, compression, predicate pushdown; partitioning theo time/key.
- 💻 **CODE**: Lưu dữ liệu sang Parquet và so sánh kích thước/ tốc độ đọc; thử partition theo date (local).

#### Ngày 77

- 📘 **LEARN**: Lakehouse basics: ACID, schema evolution, time travel; table formats (Delta Lake / Iceberg / Hudi) – khái niệm & trade-off.
- 💻 **CODE**: Viết note 1 trang: khi nào dùng warehouse vs lake vs lakehouse; nếu có môi trường: demo ghi 2 phiên bản Parquet + lưu checksum/version.

#### Ngày 78

- 📘 **LEARN**: Data Quality & Validation: profiling, schema checks, range/uniqueness, null/duplicate rules; Great Expectations / Pandera (khái niệm).
- 💻 **CODE**: Viết 5–10 rule kiểm tra dữ liệu bằng Pandera (hoặc Great Expectations) và xuất report lỗi.

#### Ngày 79

- 📘 **LEARN**: Data Versioning & Lineage: vì sao ML cần reproducibility; data lineage, metadata; giới thiệu DVC/lakeFS (khái niệm).
- 💻 **CODE**: Tạo pipeline mini: validate -> save cleaned dataset -> log metadata (hash, rows, columns) vào file JSON/YAML; fail nếu vi phạm rules.

### CAPSTONE PROJECT GIAI ĐOẠN 2

_Tổng hợp toàn bộ kiến thức Data Analysis & Feature Engineering để làm 1 mini-project end-to-end._

#### Ngày 80

- 📘 **LEARN**: Project: End-to-End Exploratory Data Analysis (EDA)
- 📘 **LEARN**: Dataset: Shopee/Tiki E-commerce Dataset hoặc Kaggle Titanic (Advanced version)
- 💻 **CODE**: 1. Data Cleaning: Xử lý null, duplicate, sai format.
- 💻 **CODE**: 2. Feature Engineering: Tạo cột mới (VD: Tách 'Title' từ 'Name', nhóm tuổi).
- 💻 **CODE**: 3. Visualization: 5-7 biểu đồ trả lời các câu hỏi Insight.
- 💻 **CODE**: 4. Correlation Analysis: Tìm các yếu tố ảnh hưởng đến mục tiêu (VD: Giá vé ảnh hưởng thế nào đến tỷ lệ sống sót).
- 💻 **CODE**: 5. Report: Xuất file Jupyter Notebook (.ipynb) sạch đẹp, có chú thích Markdown giải thích từng bước.

## Giai đoạn 3: Machine Learning Thực chiến (Classical ML)

**Thời gian:** Tuần 17 đến Tuần 26 (10 Tuần)
**Mục tiêu:** Thành thạo các thuật toán ML cốt lõi cho dữ liệu bảng (Tabular Data).
**Công cụ:** Scikit-learn, XGBoost, LightGBM, Optuna, SHAP, Imbalanced-learn

### Tuần 17: ML Overview & Linear Regression

_Hiểu luồng đi của một bài toán ML: Train, Test, Predict._

#### Ngày 81

- 📘 **LEARN**: Machine Learning Workflow: Supervised vs Unsupervised, Train/Test Split (Tại sao phải chia data?)
- 📘 **LEARN**: Data Leakage & Split đúng cách: stratified split cho classification; fit scaler/encoder chỉ trên train; pipeline để tránh leakage.
- 💻 **CODE**: Dùng sklearn.model_selection.train_test_split chia dữ liệu.

#### Ngày 82

- 📘 **LEARN**: Linear Regression (Hồi quy tuyến tính) - Lý thuyết: Phương trình đường thẳng y = ax + b, Loss Function (MSE), Gradient Descent (ôn lại)
- 💻 **CODE**: Implement Linear Regression bằng Numpy (ôn lại) vs dùng Sklearn.

#### Ngày 83

- 📘 **LEARN**: Linear Regression - Thực hành: Hệ số (Coefficients), Intercept, Đa cộng tuyến (Multicollinearity)
- 💻 **CODE**: Dự đoán giá nhà (Boston Housing/California Housing dataset).

#### Ngày 84

- 📘 **LEARN**: Polynomial Regression: Khi đường thẳng không đủ tốt (Underfitting), Tạo feature bậc cao
- 💻 **CODE**: Dùng PolynomialFeatures của sklearn để fit đường cong.

### Tuần 18: Classification (Phân loại) & Logistic Regression

_Giải quyết bài toán Yes/No (Spam hay không Spam)._

#### Ngày 85

- 📘 **LEARN**: Logistic Regression: Sigmoid Function, Decision Boundary, Tại sao dùng Log Loss?
- 💻 **CODE**: Phân loại hoa Iris (Binary Classification).

#### Ngày 86

- 📘 **LEARN**: Evaluation Metrics cho Phân loại (CỰC QUAN TRỌNG): Accuracy (dễ lừa), Precision & Recall (Quan trọng), F1-Score, Confusion Matrix
- 📘 **LEARN**: Calibration & Thresholding: xác suất dự đoán có 'đúng xác suất' không? (Platt/Isotonic); chọn threshold theo cost/precision-recall.
- 💻 **CODE**: Tính tay Precision/Recall từ Confusion Matrix.

#### Ngày 87

- 📘 **LEARN**: ROC Curve & AUC: True Positive Rate vs False Positive Rate, Threshold tuning (Chỉnh ngưỡng quyết định)
- 💻 **CODE**: Vẽ đường ROC và tính diện tích AUC.

### Tuần 19: KNN & SVM (Support Vector Machines)

_Hiểu các thuật toán dựa trên khoảng cách._

#### Ngày 88

- 📘 **LEARN**: K-Nearest Neighbors (KNN): Euclidean distance, Chọn K thế nào?, Lời nguyền của số chiều (Curse of Dimensionality)
- 💻 **CODE**: KNN classifier cho dataset chữ viết tay (MNIST nhỏ).

#### Ngày 89

- 📘 **LEARN**: Support Vector Machines (SVM): Hyperplane, Margin tối đa, Kernel Trick (biến không gian cong thành phẳng)
- 💻 **CODE**: So sánh Linear SVM vs RBF Kernel SVM.

### Tuần 20: Decision Trees & Bias-Variance Tradeoff

_Nền tảng của các thuật toán mạnh nhất hiện nay._

#### Ngày 90

- 📘 **LEARN**: Decision Trees (Cây quyết định): Entropy & Gini Impurity (Cách cây đặt câu hỏi), Pruning (Cắt tỉa cây để chống Overfitting)
- 💻 **CODE**: Visual hóa cây quyết định bằng graphviz.

#### Ngày 91

- 📘 **LEARN**: Bias vs Variance (Độ lệch vs Phương sai): Overfitting (Học vẹt) vs Underfitting (Học kém), Cách phát hiện qua Learning Curve
- 💻 **CODE**: Vẽ Learning Curve để chẩn đoán model.

#### Ngày 92

- 📘 **LEARN**: Cross-Validation (Kiểm định chéo): K-Fold CV, Stratified K-Fold (Giữ tỷ lệ nhãn)
- 📘 **LEARN**: Split theo ngữ cảnh: TimeSeriesSplit, GroupKFold (tránh rò rỉ theo user/session); Nested CV khi tuning hyperparameters.
- 💻 **CODE**: Áp dụng cross_val_score thay vì chỉ train/test split.

### Tuần 21: Ensemble Learning & Random Forest

_Sức mạnh của đám đông (Nhiều cây yếu gộp lại thành rừng mạnh)._

#### Ngày 93

- 📘 **LEARN**: Bagging & Random Forest: Bootstrap Aggregating, Tại sao Random Forest khó bị Overfit?, Feature Importance
- 💻 **CODE**: Train Random Forest Classifier. Xem feature nào quan trọng nhất.

#### Ngày 94

- 📘 **LEARN**: Ensemble Voting: Hard Voting vs Soft Voting
- 💻 **CODE**: Kết hợp kết quả của Logistic Regression, KNN và Random Forest.

### Tuần 22: Boosting Algorithms (Vũ khí tối thượng cho Tabular Data)

_Thành thạo XGBoost/LightGBM - Thứ doanh nghiệp dùng nhiều nhất._

#### Ngày 95

- 📘 **LEARN**: Boosting Concept: Học tuần tự (Sequential Learning), Sửa sai cho model trước
- 💻 **CODE**: AdaBoost cơ bản.

#### Ngày 96

- 📘 **LEARN**: XGBoost (Extreme Gradient Boosting): Tại sao XGBoost vô địch Kaggle?, Regularization tích hợp
- 💻 **CODE**: Cài đặt XGBoost, train model và sử dụng early_stopping.

#### Ngày 97

- 📘 **LEARN**: LightGBM & CatBoost: Tốc độ của LightGBM (Histogram-based), Xử lý category của CatBoost
- 💻 **CODE**: So sánh tốc độ train giữa Random Forest vs XGBoost vs LightGBM.

### Tuần 23: Unsupervised Learning

_Tìm ẩn số khi không có nhãn (Label)._

#### Ngày 98

- 📘 **LEARN**: Clustering: K-Means: Elbow Method (Chọn K tối ưu), K-Means++ init
- 💻 **CODE**: Phân nhóm khách hàng dựa trên hành vi mua sắm.

#### Ngày 99

- 📘 **LEARN**: Dimensionality Reduction: PCA: Giảm chiều dữ liệu, Giữ lại bao nhiêu thông tin (Variance explained)?
- 💻 **CODE**: Giảm dataset từ 100 chiều xuống 2 chiều để vẽ biểu đồ.

#### Ngày 100

- 📘 **LEARN**: Clustering nâng cao: DBSCAN: Phát hiện cụm hình dạng bất kỳ, Xử lý nhiễu (Noise/Outliers)
- 💻 **CODE**: So sánh kết quả K-Means vs DBSCAN trên dữ liệu hình trăng khuyết.

### Tuần 24: Advanced ML Techniques

_Xử lý các vấn đề thực tế khó nhằn._

#### Ngày 101

- 📘 **LEARN**: Imbalanced Data (Dữ liệu mất cân bằng): Tại sao Accuracy vô dụng ở đây?, Undersampling vs Oversampling (SMOTE)
- 💻 **CODE**: Dùng thư viện imbalanced-learn để sinh dữ liệu giả lập class hiếm.

#### Ngày 102

- 📘 **LEARN**: Hyperparameter Tuning: Grid Search vs Random Search, Bayesian Optimization (Optuna)
- 💻 **CODE**: Dùng Optuna để tự động tìm tham số tốt nhất cho XGBoost.

#### Ngày 103

- 📘 **LEARN**: Explainable AI (SHAP): Black box model, SHAP values: Tại sao model dự đoán người này rủi ro cao?
- 💻 **CODE**: Vẽ biểu đồ SHAP summary plot.

### Tuần 25-26: CAPSTONE PROJECT GIAI ĐOẠN 3

#### Ngày 104

- 📘 **LEARN**: Project: Credit Scoring / Customer Churn Prediction
- 📘 **LEARN**: Dataset: Telco Customer Churn (Kaggle) hoặc German Credit Data.
- 💻 **CODE**: 1. Pipeline: Xây dựng Sklearn Pipeline hoàn chỉnh (FillNA -> Scale -> Model).
- 💻 **CODE**: 2. Handling Imbalance: Áp dụng SMOTE vì số lượng khách rời bỏ thường ít.
- 💻 **CODE**: 3. Model Selection: Thử nghiệm Logistic Regression, Random Forest và XGBoost.
- 💻 **CODE**: 4. Tuning: Dùng Optuna tối ưu F1-Score (hoặc ROC-AUC).
- 💻 **CODE**: 5. Explain: Dùng SHAP để giải thích cho sếp biết: 'Yếu tố nào khiến khách hàng bỏ đi nhiều nhất?' (Giá cước? Dịch vụ CSKH?).
- 💻 **CODE**: 6. Save Model: Lưu model dạng .pkl hoặc .json để dùng sau này.

## Giai đoạn 4: Deep Learning Foundation (Updated)

**Thời gian:** Tuần 27 đến Tuần 42 (16 Tuần)
**Mục tiêu:** Xây dựng tư duy Deep Learning, thành thạo PyTorch và nắm vững kiến trúc CNN/RNN/Transformer.
**Công cụ:** PyTorch, Torchvision, OpenCV, TensorBoard / Weights & Biases, Google Colab (GPU Free)

### Tuần 27: Neural Networks (NN) - Từ con số 0

_Hiểu cấu tạo của một 'Brain cell' nhân tạo._

#### Ngày 105

- 📘 **LEARN**: Perceptron & Neuron: Mối liên hệ giữa Logistic Regression và 1 Neuron, Weights (Trọng số) & Bias
- 💻 **CODE**: Code lại 1 Neuron bằng Python thuần.

#### Ngày 106

- 📘 **LEARN**: Activation Functions (Hàm kích hoạt): Tại sao cần phi tuyến tính?, Sigmoid vs Tanh vs ReLU (Rectified Linear Unit)
- 💻 **CODE**: Vẽ đồ thị các hàm activation bằng Matplotlib.

#### Ngày 107

- 📘 **LEARN**: Multi-Layer Perceptron (MLP): Input Layer, Hidden Layers, Output Layer, Feed Forward (Lan truyền xuôi)
- 📘 **LEARN**: Computational Graph (trực giác) & shapes: forward pass tạo graph, backprop là lan truyền gradient theo graph.
- 💻 **CODE**: Xây dựng mạng MLP đơn giản phân loại dữ liệu XOR.

### Tuần 28: Backpropagation (Trái tim của DL)

_Hiểu cách model tự sửa sai (Học)._

#### Ngày 108

- 📘 **LEARN**: Loss Functions: MSE (cho Regression), Cross-Entropy Loss (cho Classification)
- 📘 **LEARN**: Jacobian/Hessian (trực giác): Jacobian là 'đạo hàm của vector'; Hessian nói về độ cong – giúp hiểu tối ưu và learning rate.
- 💻 **CODE**: Tính tay Loss của một dự đoán sai.

#### Ngày 109

- 📘 **LEARN**: Backpropagation Theory: Chain Rule (Quy tắc chuỗi - Ôn lại Calculus), Đạo hàm của Loss theo Weight
- 💻 **CODE**: Xem video 3Blue1Brown về Backpropagation (Bắt buộc).

#### Ngày 110

- 📘 **LEARN**: Optimization Algorithms: SGD (Stochastic Gradient Descent), Adam (Adaptive Moment Estimation - Dùng mặc định)
- 📘 **LEARN**: Thực chiến Optimization: Momentum/Nesterov, Weight Decay vs L2, Learning Rate Schedules, Gradient Clipping; khi nào dùng và dấu hiệu cần.
- 💻 **CODE**: So sánh tốc độ hội tụ của SGD vs Adam.

### Tuần 29-30: PyTorch Framework Mastery

_Code Deep Learning chuyên nghiệp & Quản lý thí nghiệm._

#### Ngày 111

- 📘 **LEARN**: Tensors & Autograd: Tensor là gì? (Khác gì NumPy array?), GPU acceleration (cuda), Autograd (Tự động tính đạo hàm)
- 💻 **CODE**: Chuyển đổi qua lại giữa Numpy và Tensor. Tính đạo hàm tự động y.backward().

#### Ngày 112

- 📘 **LEARN**: PyTorch Workflow: Dataset & DataLoader: Class Dataset (len, getitem), DataLoader (Batching, Shuffling)
- 💻 **CODE**: Viết custom Dataset để load ảnh từ folder.

#### Ngày 113

- 📘 **LEARN**: Building Model: nn.Module: Hàm **init** và forward(), nn.Linear, nn.Sequential
- 💻 **CODE**: Viết class ImageClassifier kế thừa nn.Module.

#### Ngày 114

- 📘 **LEARN**: Training Loop & Visualization: 5 bước chuẩn: Forward -> Loss -> Zero_grad -> Backward -> Step, Sử dụng TensorBoard để vẽ biểu đồ Loss realtime
- 💻 **CODE**: Tích hợp TensorBoardWriter vào vòng lặp train.

#### Ngày 115

- 📘 **LEARN**: Save/Load & Project MNIST: torch.save (state_dict), torch.load (Resume training)
- 💻 **CODE**: Project: Handwritten Digit Recognition (Full pipeline: Train -> Save -> Load -> Predict).

### Tuần 31-33: Computer Vision (CNN)

_Xử lý dữ liệu hình ảnh & Autoencoders._

#### Ngày 116

- 📘 **LEARN**: Convolution Operation (Tích chập): Kernel/Filter, Stride, Padding, Tại sao CNN tốt hơn MLP cho ảnh?
- 💻 **CODE**: Tính tay kết quả tích chập của ma trận 5x5 với filter 3x3.

#### Ngày 117

- 📘 **LEARN**: Pooling Layers & Architecture: Max Pooling vs Average Pooling, Cấu trúc kinh điển: Conv -> Relu -> Pool
- 💻 **CODE**: Xây dựng mô hình LeNet-5 cổ điển.

#### Ngày 118

- 📘 **LEARN**: Modern Architectures: ResNet: Vanishing Gradient Problem, Skip Connections (Residual Block), Tại sao ResNet sâu được?
- 💻 **CODE**: Dùng torchvision.models.resnet18 (pretrained=True).

#### Ngày 119

- 📘 **LEARN**: Autoencoders (Intro to Generative): Encoder - Decoder Architecture, Latent Space (Không gian ẩn), Ứng dụng: Khử nhiễu ảnh (Denoising)
- 💻 **CODE**: Xây dựng Autoencoder đơn giản để nén và giải nén ảnh MNIST.

#### Ngày 120

- 📘 **LEARN**: Transfer Learning & Object Detection Intro: Fine-tuning vs Feature Extraction, Khái niệm YOLO (You Only Look Once)
- 💻 **CODE**: Dùng ResNet đã học ImageNet để phân loại Chó/Mèo.

### Tuần 34-36: Sequence Models (RNN & NLP Foundation)

_Xử lý dữ liệu chuỗi (Text, Time Series)._

#### Ngày 121

- 📘 **LEARN**: Text Preprocessing: Tokenization, Stopwords, Stemming/Lemmatization, One-hot encoding text
- 💻 **CODE**: Dùng thư viện NLTK hoặc spaCy để xử lý câu văn.

#### Ngày 122

- 📘 **LEARN**: Word Embeddings: Tại sao One-hot tệ?, Word2Vec idea, Embedding Layer trong PyTorch
- 💻 **CODE**: Visual hóa vector từ vựng (King - Man + Woman = Queen).

#### Ngày 123

- 📘 **LEARN**: RNN (Recurrent Neural Networks): Hidden State (Trí nhớ ngắn hạn), Vấn đề Vanishing Gradient trong RNN
- 💻 **CODE**: Viết RNN đơn giản dự đoán ký tự tiếp theo.

#### Ngày 124

- 📘 **LEARN**: LSTM & GRU: Gates (Cổng quên, cổng nhập), Long Short-Term Memory
- 💻 **CODE**: Phân loại cảm xúc bình luận phim (IMDB) dùng LSTM.

### Tuần 37-38: Attention & Transformers (Cầu nối đến LLM)

_Hiểu kiến trúc đã thay đổi thế giới AI._

#### Ngày 125

- 📘 **LEARN**: Seq2Seq & Attention Mechanism: Encoder-Decoder Architecture, Bahdanau Attention (Tại sao phải focus vào từng phần?)
- 💻 **CODE**: Minh họa cơ chế Attention bằng heatmap.

#### Ngày 126

- 📘 **LEARN**: Transformer Architecture (Paper: Attention is All You Need): Self-Attention, Multi-Head Attention, Positional Encoding
- 💻 **CODE**: Đọc và chạy thử code Transformer PyTorch tutorial.

#### Ngày 127

- 📘 **LEARN**: BERT vs GPT: Encoder-only (BERT - Hiểu ngữ cảnh), Decoder-only (GPT - Sinh văn bản)
- 💻 **CODE**: Dùng HuggingFace transformers load thử BERT-base.

### Tuần 39-40: Training Tricks & Optimization

_Làm sao để model hội tụ tốt hơn và tránh Overfitting._

#### Ngày 128

- 📘 **LEARN**: Regularization: Dropout (Tắt ngẫu nhiên nơ-ron), L1/L2 Regularization (Weight decay)
- 💻 **CODE**: Thêm Dropout layer vào model và so sánh kết quả.

#### Ngày 129

- 📘 **LEARN**: Normalization: Batch Normalization (Chuẩn hóa theo batch), Layer Normalization (Dùng cho RNN/Transformer)
- 💻 **CODE**: Thêm BatchNorm2d vào CNN model.

#### Ngày 130

- 📘 **LEARN**: Learning Rate Scheduling: Learning Rate Decay, Warm-up steps
- 💻 **CODE**: Sử dụng StepLR scheduler trong PyTorch.

### Tuần X (Bổ sung): Multimodal AI – Audio, Video & CLIP

_Làm quen với xử lý Audio/Video và mô hình đa phương thức (kết hợp Text + Image), mở rộng khả năng làm dự án AI thực tế._

#### Ngày 131

- 📘 **LEARN**: Nhập môn xử lý Audio: sóng âm, sampling rate, spectrogram, Mel-spectrogram. Thư viện librosa/torchaudio.
- 💻 **CODE**: Dùng librosa để đọc file .wav, hiển thị waveform và Mel-spectrogram. Lưu hình ra file PNG.

#### Ngày 132

- 📘 **LEARN**: Speech-to-Text (STT): tổng quan mô hình Whisper (OpenAI) và các pipeline STT phổ biến.
- 💻 **CODE**: Dùng thư viện/CLI Whisper (hoặc model STT trên HuggingFace) để chuyển 1 file audio ngắn thành text. So sánh chất lượng với transcript chuẩn.

#### Ngày 133

- 📘 **LEARN**: Xử lý Video bằng OpenCV + Deep Learning: đọc video, trích frame, basic object detection/tracking.
- 💻 **CODE**: Viết script: đọc video, trích frame mỗi 1s, chạy sẵn một model object detection (VD: YOLO pre-trained) trên từng frame, vẽ bounding box và lưu video output.

#### Ngày 134

- 📘 **LEARN**: Multimodal Models: kiến trúc CLIP (Contrastive Language-Image Pretraining). Ý tưởng embedding chung cho Text & Image.
- 💻 **CODE**: Dùng CLIP (OpenAI/HF) để: (1) Encode một list caption và một list hình; (2) Tìm caption phù hợp nhất cho mỗi hình (image-text retrieval).

#### Ngày 135

- 📘 **LEARN**: Thiết kế bài toán Multimodal thực tế: recommendation dựa trên cả ảnh + mô tả, tìm kiếm hình ảnh bằng câu tự nhiên.
- 💻 **CODE**: Mini Project: Xây một demo simple search – nhập câu tiếng Việt/Anh, dùng CLIP để tìm ra top-k hình ảnh phù hợp nhất trong một thư viện ảnh nhỏ. Viết README mô tả kiến trúc.

### Tuần 41-42: CAPSTONE PROJECT: Multimodal Content Search & Understanding Platform

_Xây dựng nền tảng tìm kiếm nội dung đa phương thức, có thể xử lý và tích hợp Text, Image, Audio, Video, từ đó nâng cao khả năng làm dự án lớn và thực chiến._

#### Ngày 136

- 💻 **DEFINE**: Xác định bài toán cụ thể (ví dụ: Visual Search, Video Analysis, Content Recommendation hoặc Interview Analysis).
- 💻 **COLLECT_DATA**: Thu thập dataset phù hợp (ít nhất 300-500 items), có thể dùng dữ liệu mở hoặc tự tạo.

#### Ngày 137

- 💻 **PREPROCESS**: Tiền xử lý dữ liệu: chuyển đổi audio thành spectrogram, trích xuất ảnh, chuẩn bị text.
- 💻 **EMBED**: Encode dữ liệu bằng các mô hình phù hợp: CLIP cho ảnh + text, Wav2Vec2 cho audio, ViT cho ảnh, speech models cho audio.

#### Ngày 138

- 💻 **BUILD_MODEL**: Huấn luyện hoặc fine-tune mô hình multimodal fusion (ví dụ: dùng CLIP hoặc mô hình fusion custom).

#### Ngày 139

- 💻 **EVALUATE**: Đánh giá hệ thống: recall@K, precision, visualization bằng t-SNE hoặc UMAP.

#### Ngày 140

- 💻 **DEPLOY**: Xây dựng API (FastAPI), đóng gói bằng Docker, triển khai thử trên cloud hoặc local.

#### Ngày 141

- 💻 **DOCUMENT**: Viết tài liệu hướng dẫn, design architecture, kết quả, và demo trực tuyến (ví dụ: Streamlit).

## Giai đoạn 5: LLM, RAG & AI Agents (Generative AI) - Updated

**Thời gian:** Tuần 43 đến Tuần 62 (20 Tuần)
**Mục tiêu:** Làm chủ công nghệ Generative AI: Từ RAG nâng cao, GraphRAG đến Fine-tuning và Multi-Agent Systems.
**Công cụ:** LangChain, LangGraph, LlamaIndex, ChromaDB / Qdrant, Neo4j (Graph DB), HuggingFace PEFT (LoRA), Ollama (Local LLM), Ragas (Evaluation)

### Tuần 43-44: LLM Fundamentals & Structured Output

_Hiểu cách giao tiếp và điều khiển mô hình trả về dữ liệu có cấu trúc._

#### Ngày 148

- 📘 **LEARN**: LLM Architecture Recap: Pre-training vs Fine-tuning, Context Window & Tokens (Cách tính tiền), Temperature, Top-P (Tham số sinh văn bản)
- 📘 **LEARN**: Tokenization 101: BPE/SentencePiece, token vs word, OOV; vì sao token count ảnh hưởng chi phí và giới hạn context.
- 💻 **CODE**: Sử dụng Tiktoken để đếm số token của đoạn văn.

#### Ngày 149

- 📘 **LEARN**: Structured Output (JSON Mode): Tại sao LLM cần trả về JSON?, Function Calling để ép kiểu dữ liệu, Thư viện Instructor hoặc Pydantic OutputParser
- 📘 **LEARN**: Attention & Positional Encoding (trực giác): vì sao transformer 'nhớ' được ngữ cảnh; context window và KV cache (high-level).
- 💻 **CODE**: Viết prompt ép model trích xuất thông tin từ CV ra file JSON đúng format.

#### Ngày 150

- 📘 **LEARN**: Running Local LLMs: Cài đặt Ollama / LM Studio, Quantization (GGUF) - Tại sao chạy được Llama 3 trên laptop?
- 📘 **LEARN**: Decoding Strategies: temperature/top-k/top-p, repetition penalty, stop sequences; deterministic vs sampling.
- 📘 **LEARN**: LLM Security intro: Prompt Injection patterns, data exfiltration risks; nguyên tắc system prompt, input/output filtering cơ bản.
- 💻 **CODE**: Viết Python script gọi API tới localhost Ollama.

### Tuần 45-47: RAG Foundation (Retrieval Augmented Generation)

_Cho LLM 'học' dữ liệu riêng của bạn mà không cần train lại._

#### Ngày 151

- 📘 **LEARN**: Vector Embeddings: Biến văn bản thành Vector số thực, Cosine Similarity (Đo độ tương đồng), Mô hình Embedding (OpenAI text-embedding-3 vs BGE-M3)
- 💻 **CODE**: Viết hàm tìm kiếm ngữ nghĩa (Semantic Search) đơn giản.

#### Ngày 152

- 📘 **LEARN**: Vector Databases: Cấu trúc Vector DB (ChromaDB, Weaviate), CRUD operations trên Vector DB
- 💻 **CODE**: Lưu 100 trang tài liệu PDF vào ChromaDB.

#### Ngày 153

- 📘 **LEARN**: RAG Pipeline cơ bản: Quy trình: Load -> Split -> Embed -> Store -> Retrieve -> Generate, Chunking Strategies (Cắt nhỏ văn bản thế nào cho đúng?)
- 💻 **CODE**: Xây dựng Chatbot hỏi đáp tài liệu đơn giản bằng LangChain.

### Tuần 48-50: Advanced RAG & GraphRAG

_Khắc phục nhược điểm của RAG cơ bản bằng Semantic + Knowledge Graph._

#### Ngày 154

- 📘 **LEARN**: Hybrid Search: Kết hợp Keyword Search (BM25) + Vector Search, Tại sao Vector Search thất bại với từ khóa chính xác?
- 💻 **CODE**: Implement Hybrid Search dùng Qdrant hoặc Weaviate.

#### Ngày 155

- 📘 **LEARN**: Re-ranking (Sắp xếp lại): Cross-Encoder models (Cohere Rerank / BGE-Reranker), Lọc kết quả rác trước khi gửi cho LLM
- 💻 **CODE**: Thêm bước Re-ranking vào pipeline RAG để tăng độ chính xác.

#### Ngày 156

- 📘 **LEARN**: GraphRAG (Knowledge Graph RAG): Hạn chế của Vector Search (Mất mối quan hệ thực thể), Knowledge Graph là gì? (Neo4j), Kết hợp Graph + Vector
- 💻 **CODE**: Dùng LlamaIndex hoặc Microsoft GraphRAG để truy vấn mối quan hệ phức tạp.

### Tuần 51-53: LangChain & LlamaIndex Deep Dive

_Thành thạo framework phát triển ứng dụng LLM số 1 hiện nay._

#### Ngày 157

- 📘 **LEARN**: LangChain LCEL: LangChain Expression Language (Pipe syntax | ), Runnables & Chains
- 💻 **CODE**: Viết Chain: Prompt | Model | OutputParser.

#### Ngày 158

- 📘 **LEARN**: Memory & History: Quản lý lịch sử chat (ConversationBufferMemory), Lưu history vào Redis/Postgres
- 💻 **CODE**: Tạo Chatbot nhớ được tên người dùng qua nhiều lượt chat.

#### Ngày 159

- 📘 **LEARN**: LlamaIndex for Data: Data Connectors (Lấy dữ liệu từ Notion, Slack, SQL), LlamaIndex Query Engine
- 💻 **CODE**: Xây dựng hệ thống hỏi đáp trên cơ sở dữ liệu SQL (Text-to-SQL).

### Tuần 54-56: AI Agents & Orchestration (LangGraph)

_Xây dựng AI chủ động thực hiện hành động (Tương lai của AI)._

#### Ngày 160

- 📘 **LEARN**: Tool Calling (Function Calling): Dạy LLM cách dùng công cụ (Calculator, Google Search API), Định nghĩa Tools bằng Pydantic
- 💻 **CODE**: Tạo Agent biết tự tính toán và search web.

#### Ngày 161

- 📘 **LEARN**: LangGraph Basics: Stateful Agents (Agent có trạng thái), Nodes & Edges (Quy trình dạng đồ thị), Cyclic Graphs (Vòng lặp suy nghĩ)
- 💻 **CODE**: Xây dựng luồng Agent: Plan -> Execute -> Reflect (Tự kiểm tra) -> Output.

#### Ngày 162

- 📘 **LEARN**: Multi-Agent Systems: Phân chia nhiệm vụ: Researcher Agent & Writer Agent, Supervisor Agent (Quản lý chung)
- 💻 **CODE**: Xây dựng đội ngũ Agent tự động viết bài blog nghiên cứu.

### Tuần 57-58: LLM Evaluation (Kiểm thử chất lượng)

_Làm sao biết Chatbot trả lời đúng hay sai?_

#### Ngày 163

- 📘 **LEARN**: RAG Evaluation Metrics: Faithfulness (Trung thực với dữ liệu nguồn), Answer Relevance (Trả lời đúng trọng tâm), Context Recall (Tìm đủ thông tin không)
- 💻 **CODE**: Dùng thư viện Ragas để chấm điểm hệ thống RAG.

#### Ngày 164

- 📘 **LEARN**: Observability (Quan sát): Tracing với LangSmith hoặc Arize Phoenix, Debug từng bước chạy của Chain
- 💻 **CODE**: Tích hợp LangSmith để theo dõi token usage và latency.

### Tuần 59-60: Fine-tuning & Optimization (Nâng cao)

_Tùy biến Model cho tác vụ chuyên biệt._

#### Ngày 165

- 📘 **LEARN**: PEFT & LoRA: Parameter-Efficient Fine-Tuning (Chỉ train < 1% tham số), Low-Rank Adaptation (LoRA)
- 💻 **CODE**: Chuẩn bị dataset định dạng JSONL cho fine-tuning.

#### Ngày 166

- 📘 **LEARN**: Fine-tuning & Serving Optimization: Sử dụng thư viện Unsloth (Tối ưu tốc độ train x2), Quantization for Serving (AWQ / GPTQ) để giảm chi phí VRAM
- 💻 **CODE**: Fine-tune model Llama-3 và export ra định dạng GGUF để chạy tiết kiệm.

### Tuần Y (Bổ sung): Advanced LLM Training – RLHF & DPO

_Hiểu và thực hành các kỹ thuật tối ưu LLM hiện đại dựa trên phản hồi con người: RLHF và DPO._

#### Ngày 167

- 📘 **LEARN**: Tổng quan RLHF (Reinforcement Learning from Human Feedback): pipeline 3 bước – (1) SFT, (2) Reward Model, (3) RL (PPO).
- 📘 **LEARN**: Đọc tóm tắt paper InstructGPT hoặc RLHF overview, ghi chú lại flow dữ liệu và mục tiêu của từng bước.

#### Ngày 168

- 📘 **LEARN**: Reward Model: cách huấn luyện model phân biệt giữa câu trả lời tốt/xấu dựa trên cặp preference (A tốt hơn B).
- 💻 **CODE**: Chuẩn bị một mini-dataset gồm các cặp (prompt, answer_good, answer_bad) dạng JSON/CSV để dùng cho reward model hoặc DPO.

#### Ngày 169

- 📘 **LEARN**: Giới thiệu thư viện TRL (HuggingFace) – hỗ trợ PPO, DPO. So sánh high-level RLHF vs DPO (Direct Preference Optimization).
- 💻 **CODE**: Dùng TRL hoặc thư viện tương tự để chạy thử một vòng PPO rất nhỏ trên model nhỏ (VD: distilGPT2) với 5–10 mẫu preference (demo).

#### Ngày 170

- 📘 **LEARN**: DPO (Direct Preference Optimization): động lực ra đời, ưu điểm so với RLHF cổ điển (đơn giản hơn, ổn định hơn).
- 💻 **CODE**: Áp dụng DPO trên chính dataset preference nhỏ ở trên để tinh chỉnh một model nhỏ. So sánh output trước/sau DPO trên vài prompt.

#### Ngày 171

- 📘 **LEARN**: Các vấn đề thực tế của RLHF/DPO: chất lượng dữ liệu human feedback, bias, over-optimization, chi phí compute.
- 💻 **CODE**: Viết báo cáo ngắn (Markdown/Jupyter): mô tả pipeline RLHF/DPO bạn đã thử, các hạn chế do dataset nhỏ, và kế hoạch mở rộng nếu có GPU + dữ liệu thật.

### Tuần 61-62: CAPSTONE PROJECT GIAI ĐOẠN 5

#### Ngày 172

- 📘 **LEARN**: Project: Intelligent Legal/Medical Assistant (Agentic RAG)
- 💻 **CODE**: 1. Data Pipeline: Crawl và xử lý sạch dữ liệu văn bản pháp luật/y khoa.
- 💻 **CODE**: 2. Hybrid RAG: Kết hợp Vector Search + Keyword Search + Re-ranking.
- 💻 **CODE**: 3. GraphRAG (Optional): Xây dựng Knowledge Graph cho các điều luật liên quan nhau.
- 💻 **CODE**: 4. Agent Workflow (LangGraph): Agent có khả năng hỏi lại user nếu thiếu thông tin (Human-in-the-loop).
- 💻 **CODE**: 5. Evaluation: Viết bộ test case gồm 50 câu hỏi khó để đánh giá độ chính xác.
- 💻 **CODE**: 6. UI: Giao diện Chat chuyên nghiệp (Streamlit/Chainlit).

## Giai đoạn 6: Software Engineering & Data Ops (Updated)

**Thời gian:** Tuần 63 đến Tuần 74 (12 Tuần)
**Mục tiêu:** Xây dựng Backend vững chắc, bảo mật, đóng gói ứng dụng tối ưu và tự động hóa quy trình (CI/CD).
**Công cụ:** FastAPI, Uvicorn/Gunicorn, Docker & Docker Compose, Kubernetes (K8s Basic), GitHub Actions, PostgreSQL (pgvector), Redis, Celery / RabbitMQ

### Tuần 63-64: Backend API Development & Security

_Viết API hiệu năng cao, bảo mật và chuẩn chỉnh._

#### Ngày 173

- 📘 **LEARN**: FastAPI, Pydantic & Config Management: Pydantic Settings (Quản lý biến môi trường .env an toàn), Dependency Injection trong FastAPI (Clean Architecture), Middleware (CORS, Logging)
- 💻 **CODE**: Viết API load config từ file .env và log mọi request vào file.

#### Ngày 174

- 📘 **LEARN**: Authentication & Security: OAuth2 với Password Flow, JWT (JSON Web Tokens) - Tạo và xác thực token, Rate Limiting (Chống DDOS đơn giản)
- 💻 **CODE**: Tích hợp đăng nhập JWT vào API, bảo vệ route /admin.

#### Ngày 175

- 📘 **LEARN**: Asyncio & Streaming Response: Server-Sent Events (SSE) cho Chatbot, Websockets (Giao tiếp 2 chiều realtime), Xử lý tác vụ nền (Background Tasks)
- 💻 **CODE**: Tạo API chat trả về từng token (Streaming) giống ChatGPT.

### Tuần 65-66: Containerization (Docker Advanced)

_Tối ưu hóa Docker Image cho môi trường Production._

#### Ngày 176

- 📘 **LEARN**: Docker Best Practices: Multi-stage builds (Giảm size image từ 1GB -> 200MB), .dockerignore (Tránh copy file rác), Non-root user (Bảo mật container)
- 💻 **CODE**: Viết Dockerfile multi-stage tối ưu cho ứng dụng Python.

#### Ngày 177

- 📘 **LEARN**: Docker for AI/GPU: NVIDIA Container Toolkit (Chạy model trên GPU docker), Caching pip packages để build nhanh hơn
- 💻 **CODE**: Build image Docker hỗ trợ CUDA để chạy PyTorch.

#### Ngày 178

- 📘 **LEARN**: Docker Compose for Dev Environment: Orchestrate API + DB + Redis + Worker, Healthchecks (Đợi DB khởi động xong mới chạy API)
- 💻 **CODE**: Setup docker-compose.yml chạy full stack local.

### Tuần 67-68: Database & Async Workers

_Xử lý dữ liệu lớn và tác vụ nặng không làm treo API._

#### Ngày 179

- 📘 **LEARN**: PostgreSQL & pgvector: Thiết kế Schema tối ưu cho Vector Search, Indexing (HNSW index) để tìm kiếm nhanh, Migrations với Alembic (Quản lý thay đổi DB)
- 💻 **CODE**: Tạo bảng lưu Embeddings và query tìm kiếm vector tương đồng.

#### Ngày 180

- 📘 **LEARN**: Redis & Async Workers (Celery): Redis Caching strategy, Message Queue (RabbitMQ/Redis), Celery (Xử lý tác vụ nặng như parse PDF, train model)
- 💻 **CODE**: Setup Worker xử lý việc upload file PDF ở background.

### Tuần 69-70: Testing & CI/CD

_Tự động hóa quy trình kiểm thử và deploy._

#### Ngày 181

- 📘 **LEARN**: Automated Testing (Pytest): Unit Test vs Integration Test, Test Client (FastAPI) & Fixtures, Mocking External APIs (Không gọi OpenAI thật khi test)
- 💻 **CODE**: Viết test case coverage > 80% cho module Auth.

#### Ngày 182

- 📘 **LEARN**: GitHub Actions (CI/CD): Pipeline: Lint -> Test -> Build -> Push Docker Hub, Quản lý Secrets trên GitHub
- 💻 **CODE**: Setup workflow tự động build image khi push vào nhánh main.

### Tuần 71-72: Orchestration Intro (Kubernetes)

_Hiểu khái niệm để deploy lên Cloud (AWS EKS / GKE)._

#### Ngày 183

- 📘 **LEARN**: Kubernetes Concepts: Pod, Deployment, Service, Ingress, ConfigMap & Secrets (Quản lý cấu hình K8s)
- 💻 **CODE**: Viết manifest deployment.yaml và service.yaml.

#### Ngày 184

- 📘 **LEARN**: Deploying & Scaling: Horizontal Pod Autoscaling (HPA), Rolling Updates (Deploy không downtime)
- 💻 **CODE**: Deploy ứng dụng lên cụm K8s local (Minikube).

### Tuần 73-74: CAPSTONE PROJECT GIAI ĐOẠN 6

#### Ngày 185

- 📘 **LEARN**: Project: Production-Grade GenAI Backend
- 💻 **CODE**: 1. Security: Tích hợp JWT Auth, Rate Limiting, CORS.
- 💻 **CODE**: 2. Async Architecture: API nhận request -> đẩy vào Queue -> Worker xử lý -> API trả kết quả (hoặc Webhook).
- 💻 **CODE**: 3. Database: Postgres (User/Data) + Qdrant (Vector) + Redis (Cache/Queue).
- 💻 **CODE**: 4. Docker: Multi-stage build, image size < 500MB (nếu không kèm model) hoặc tối ưu layer model.
- 💻 **CODE**: 5. CI/CD: Pipeline test và build tự động.
- 💻 **CODE**: 6. Monitoring: Tích hợp Prometheus/Grafana cơ bản để đo API latency.

## Giai đoạn 7: MLOps & Production Optimization (Updated)

**Thời gian:** Tuần 75 đến Tuần 86 (12 Tuần)
**Mục tiêu:** Triển khai model chuẩn chỉnh (IaC), tối ưu chi phí và giám sát an toàn hệ thống.
**Công cụ:** AWS (EC2, SageMaker, Lambda), Terraform / AWS CDK (Infrastructure as Code), vLLM / Triton Server, MLflow, Prometheus & Grafana, NVIDIA NeMo Guardrails (AI Security)

### Tuần 75-76: Model Serving Optimization

_Tối ưu hóa độ trễ (Latency) và thông lượng (Throughput) cho LLM._

#### Ngày 186

- 📘 **LEARN**: Inference Engines (vLLM), PagedAttention & Continuous Batching, Thiết lập vLLM server cho Llama-3/Mistral
- 💻 **CODE**: Triển khai vLLM server dockerized, expose API chuẩn OpenAI.

#### Ngày 187

- 📘 **LEARN**: Triton Inference Server, Kiến trúc NVIDIA Triton, Model Ensemble (Kết hợp nhiều model: Preprocess -> Model -> Postprocess)
- 💻 **CODE**: Cấu hình model repository cho Triton chạy model ONNX.

#### Ngày 188

- 📘 **LEARN**: Load Testing (Stress Test), Locust / JMeter, Đo đạc RPS (Requests per second) và P99 Latency
- 💻 **CODE**: Viết script Locust giả lập 1000 user chat cùng lúc để tìm điểm chết của server.

### Tuần 77-78: Quantization & Cost Optimization

_Chạy model lớn trên phần cứng rẻ tiền._

#### Ngày 189

- 📘 **LEARN**: Quantization Techniques, GGUF (CPU Inference), AWQ / GPTQ (GPU Inference tối ưu), KV Cache Quantization
- 💻 **CODE**: Convert model Llama-3-8B FP16 sang AWQ 4-bit giúp giảm 60% VRAM.

#### Ngày 190

- 📘 **LEARN**: Distillation & Pruning, Teacher-Student Training (Model nhỏ học từ model to), Structural Pruning (Cắt bỏ nơ-ron thừa)
- 💻 **CODE**: Thực hành Distillation: Dạy model TinyLlama học theo GPT-4.

### Tuần 79-81: Cloud Infrastructure & IaC (Chuyên nghiệp)

_Quản lý hạ tầng bằng Code (Không click tay)._

#### Ngày 191

- 📘 **LEARN**: AWS Compute for AI, EC2 G4dn/G5 instances (NVIDIA GPU), AWS Spot Instances (Bid giá rẻ), Deep Learning AMI (Setup sẵn driver)
- 💻 **CODE**: Launch một Spot Instance giá rẻ để train model.

#### Ngày 192

- 📘 **LEARN**: Infrastructure as Code (IaC), Khái niệm IaC (Terraform hoặc AWS CDK), Tại sao không nên config thủ công trên Console?
- 💻 **CODE**: Viết file Terraform đơn giản để tự động tạo EC2 và Security Group.

#### Ngày 193

- 📘 **LEARN**: Serverless Inference, AWS Lambda (Cho model nhỏ/CPU), SageMaker Serverless Inference, RunPod / Modal (Alternative providers)
- 💻 **CODE**: Deploy hàm xử lý ảnh đơn giản lên AWS Lambda + EFS.

### Tuần 82-83: MLOps Lifecycle (Tracking & CI/CD)

_Tự động hóa quy trình huấn luyện và triển khai._

#### Ngày 194

- 📘 **LEARN**: Experiment Tracking (MLflow), Logging metrics/params, Artifact Storage (S3), MLflow UI
- 💻 **CODE**: Setup MLflow Server remote (trên EC2) kết nối với S3 bucket.

#### Ngày 195

- 📘 **LEARN**: Model Registry & CD, Promote model (Staging -> Production), Trigger deploy khi có model mới
- 💻 **CODE**: GitHub Actions: Tự động deploy model khi chuyển trạng thái sang 'Production' trong MLflow.

### Tuần 84-85: Monitoring & AI Security (Guardrails)

_Giám sát sức khỏe và đảm bảo an toàn cho AI._

#### Ngày 196

- 📘 **LEARN**: AI Security (Guardrails), Prompt Injection Attacks, Input/Output Filtering (Lọc nội dung độc hại/nhạy cảm), NVIDIA NeMo Guardrails
- 💻 **CODE**: Tích hợp Guardrails chặn chatbot nói bậy hoặc tiết lộ thông tin cá nhân.

#### Ngày 197

- 📘 **LEARN**: System Monitoring, Prometheus (Thu thập metrics), Grafana (Vẽ biểu đồ), Drift Detection (Phát hiện model bị sai dần theo thời gian)
- 💻 **CODE**: Setup Dashboard Grafana cảnh báo khi GPU > 90% hoặc API error rate > 1%.

### Tuần 86: CAPSTONE PROJECT GIAI ĐOẠN 7

_Xây dựng nền tảng LLM nội bộ hoàn chỉnh trên AWS._

#### Ngày 198

- 📘 **LEARN**: Project: Production-Grade LLM Platform
- 💻 **CODE**: 1. Infrastructure: Dùng Terraform dựng VPC, EC2 (vLLM), RDS (Database).
- 💻 **CODE**: 2. Deployment: Deploy model Llama-3 dạng Quantized (AWQ) trên Docker.
- 💻 **CODE**: 3. Security: Tích hợp NeMo Guardrails chặn Prompt Injection.
- 💻 **CODE**: 4. Pipeline: Auto-deploy khi update code mới (GitHub Actions).
- 💻 **CODE**: 5. Monitoring: Full dashboard Grafana theo dõi token/s, latency và chi phí ước tính.

## Giai đoạn 8 (Bổ sung): ML System Design & Scalable AI Engineering

**Thời gian:** 3–4 Tuần | Tập trung System Design, Distributed Training & Production
**Mục tiêu:** Xây dựng tư duy kiến trúc hệ thống AI end-to-end, chịu tải cao, dễ mở rộng; hiểu cách train/serve model lớn trên nhiều GPU/máy.
**Công cụ:** AWS/GCP/Azure (hoặc Local + Docker), Kubernetes (cơ bản), Torch DDP/FSDP hoặc DeepSpeed, Prometheus/Grafana (hoặc tương đương)

### Tuần n: ML System Design Fundamentals

_Nắm được các thành phần chính của một hệ thống ML end-to-end từ Data đến Monitoring._

#### Ngày 199

- 📘 **LEARN**: ML System Lifecycle: Data → ETL → Training → Evaluation → Deployment → Monitoring → Feedback Loop.
- 💻 **CODE**: Vẽ sơ đồ kiến trúc (bằng draw.io, Excalidraw hoặc Mermaid) cho một hệ thống recommendation đơn giản (offline batch prediction).

#### Ngày 200

- 📘 **LEARN**: Batch vs Online vs Streaming Inference: ưu/nhược điểm, ví dụ use-case cho từng loại.
- 💻 **CODE**: Thiết kế 2 biến thể cho cùng một bài toán (VD: fraud detection): (1) Batch inference hằng ngày; (2) Real-time API. Viết README so sánh.

#### Ngày 201

- 📘 **LEARN**: Feature Store & Data Contract: quản lý feature dùng chung cho training & serving, đảm bảo không bị training-serving skew.
- 💻 **CODE**: Thiết kế (dạng JSON/YAML) schema cho một bộ feature dùng lại được (user_features, item_features, interaction_features) và mô tả cách cập nhật.

#### Ngày 202

- 📘 **LEARN**: System Design Interview cho ML/AI: cách phân tích yêu cầu, vẽ kiến trúc, chọn trade-off.
- 💻 **CODE**: Viết một bản design doc ngắn (1–2 trang) cho hệ thống AI bất kỳ bạn đã làm ở Capstone trước: mục tiêu, kiến trúc, trade-off.

### Tuần n: Distributed Training & Large-scale Serving

_Hiểu cách huấn luyện và phục vụ model lớn trên nhiều GPU/máy, giảm lỗi Out-Of-Memory và tăng throughput._

#### Ngày 203

- 📘 **LEARN**: Tổng quan Distributed Training: Data Parallel, Model Parallel, Pipeline Parallel. Các thư viện: PyTorch DDP, FSDP, DeepSpeed.
- 💻 **CODE**: Đọc và chạy ví dụ official PyTorch DDP trên 2 GPU (hoặc mô phỏng multi-process trên 1 GPU/CPU nếu máy yếu). Ghi chú lại cấu trúc code.

#### Ngày 204

- 📘 **LEARN**: Memory Optimization: gradient checkpointing, mixed precision (FP16/BF16), offloading parameter sang CPU/disk.
- 💻 **CODE**: Lấy một model tương đối lớn (VD: LLM nhỏ, Vision Transformer), so sánh sử dụng bộ nhớ khi: (1) FP32 full; (2) mixed precision; (3) gradient checkpointing.

#### Ngày 205

- 📘 **LEARN**: Model Serving: so sánh REST vs gRPC, single model server vs model gateway. Khái niệm autoscaling, load balancing.
- 💻 **CODE**: Đóng gói một model đã huấn luyện thành service (FastAPI/Flask + Docker). Đo latency khi gọi nhiều request song song (dùng locust/ab).

#### Ngày 206

- 📘 **LEARN**: Monitoring & Observability cho hệ thống AI: metrics (latency, error rate), model metrics (drift, data quality), logging.
- 💻 **CODE**: Thêm logging cơ bản và thu thập metric (VD: bằng Prometheus client hoặc custom logs) cho service model. Vẽ bảng/đồ thị đơn giản từ log.

### Tuần n–n+1: Capstone – Thiết kế & triển khai hệ thống AI lớn

_Tổng hợp toàn bộ kiến thức để thiết kế một hệ thống AI gần với sản phẩm thực tế, có khả năng mở rộng._

#### Ngày 207

- 📘 **LEARN**: Chọn bài toán: recommendation, search, chatbot LLM, hoặc fraud detection… theo sở thích của bạn.
- 💻 **CODE**: Viết Problem Statement & Requirement rõ ràng: loại data, SLA (latency, throughput), constraint (ngân sách, số GPU).

#### Ngày 208

- 💻 **CODE**: Thiết kế kiến trúc end-to-end chi tiết: (1) Data pipeline (batch/streaming), (2) Training pipeline, (3) Serving architecture, (4) Monitoring. Vẽ sơ đồ, mô tả từng component.

#### Ngày 209

- 💻 **CODE**: Triển khai một bản MVP: dữ liệu nhỏ + 1–2 microservice (model API, data preprocessor). Dùng Docker để chạy toàn bộ trên cùng một máy hoặc cloud rẻ.

#### Ngày 210

- 💻 **CODE**: Thực hiện load test nhỏ (giả lập 100–1000 request/phút tùy tài nguyên), ghi lại kết quả, bottleneck, và đề xuất hướng tối ưu (scale up/out, cache, batching). Viết Design Doc/Report hoàn chỉnh đưa lên GitHub.
