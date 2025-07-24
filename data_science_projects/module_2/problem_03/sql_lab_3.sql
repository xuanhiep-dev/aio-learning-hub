----- Question 1: Thêm ít nhất 10 record vào mỗi table -----
INSERT INTO `Account`(Email						,	Username		,	FullName		,	DepartmentID		,	PositionID		, 	CreateDate)
VALUES 				 ('account6@gmail.com'		,	'account6'		,	'Account 6'		,		5				,	1				,	'2020-03-05'),
					 ('account7@gmail.com'		,	'account7'		,	'Account 7'		,		1				,	2				,	'2020-03-06'),
                     ('account8@gmail.com'		,	'account8'		,	'Account 8'		,		2				,	3				,	'2020-03-07'),
                     ('account9@gmail.com'		,	'account9'		,	'Account 9'		,		3				,	4				,	'2020-03-08'),
                     ('account10@gmail.com'		,	'account10'		,	'Account 10'	,		4				,	4				,	'2020-03-09');

INSERT INTO `Group`	(  GroupName	,	CreatorID		,	CreateDate)
VALUES 				(N'Group 6'		,	5				,	'2019-03-05'),
					(N'Group 7'		,	1				,	'2020-03-06'),
                    (N'Group 8'		,	2				,	'2020-03-07'),
                    (N'Group 9'		,	3				,	'2020-03-08'),
                    (N'Group 10'	,	4				,	'2020-03-09');

INSERT INTO `GroupAccount`	(  GroupID	,	AccountID	, JoinDate	 )
VALUES 						(	2		,    1			,'2019-03-05'),
							(	6		,    3			,'2020-03-07'),
							(	4		,    8			,'2020-03-09'),
							(	4		,    7			,'2020-03-10'),
							(	5		,    6			,'2020-03-28');

INSERT INTO CategoryQuestion		(CategoryName	)
VALUES 								('Java 2'		),
									('Python'		),
									('SQL 2'		),
									('Java 3'		),
									('Java 4'		);
													
INSERT INTO Question	(Content				, CategoryID, 		TypeID		, CreatorID		, CreateDate )
VALUES 					(N'Câu hỏi về Java 2'	,	6			,   1			,   6			,'2020-04-05'),
						(N'Câu Hỏi về Python'	,	7			,   2			,   2			,'2020-04-05'),
						(N'Hỏi về SQL 2'		,	8			,   2			,   7			,'2020-04-06'),
						(N'Hỏi về Java 3'		,	9			,   1			,   8			,'2020-04-06'),
						(N'Hỏi về Java 4'		,	10			,   1			,   5			,'2020-04-06');

INSERT INTO Answer	(  Content		, QuestionID	, isCorrect	)
VALUES 				(N'Trả lời 06'	,   5			,	0		),
					(N'Trả lời 07'	,   4			,	1		),
                    (N'Trả lời 08'	,   3			,	0		),
                    (N'Trả lời 09'	,   6			,	1		),
                    (N'Trả lời 10'	,   7			,	1		);
	
INSERT INTO Exam	(`Code`			, Title						, CategoryID	, Duration	, CreatorID		, CreateDate )
VALUES 				('VTIQ006'		, N'Đề thi Java 2'			,	6			,	60		,   5			,'2019-04-05'),
					('VTIQ007'		, N'Đề thi  Python'			,	7			,	60		,   2			,'2019-04-05'),
                    ('VTIQ008'		, N'Đề thi SQL 2'			,	8			,	120		,   2			,'2019-04-07'),
                    ('VTIQ009'		, N'Đề thi Java 3'			,	9			,	60		,   3			,'2020-04-08'),
                    ('VTIQ010'		, N'Đề thi Java 4'			,	10			,	120		,   4			,'2020-04-10');
                    
                    
INSERT INTO ExamQuestion(ExamID	, 	QuestionID	) 
VALUES 					(	6	,		6		),
						(	7	,		7		), 
						(	8	,		8		), 
						(	9	,		9		), 
						(	10	,		10		);

----- Question 2: Lấy ra tất cả các phòng ban Department -----
SELECT *
FROM Department;

----- Question 3: Lấy ra id của phòng ban "Sale" -----
SELECT 	DepartmentID
FROM 	Department
WHERE 	DepartmentName = "Sale";

----- Question 4: Lấy ra thông tin account có full name dài nhất -----
SELECT *
FROM `Account`
WHERE LENGTH(FullName) = 	(SELECT MAX(LENGTH(FullName))
							FROM `Account`);

----- Question 5: Lấy ra thông tin account có full name dài nhất và thuộc phòng ban có id = 3 -----
SELECT *
FROM `Account`
WHERE LENGTH(FullName) = 	(SELECT MAX(LENGTH(FullName))
							FROM `Account`)
	  AND DepartmentID = 3;

----- Question 6: Lấy ra tên group đã tham gia trước ngày 20/12/2019 -----
SELECT *
FROM `Group`
WHERE CreateDate < '2019-12-20';

----- Question 7: Lấy ra ID của question có >= 4 câu trả lời -----
SELECT QuestionID
FROM Question
WHERE QuestionID =  (SELECT QuestionID
					FROM Answer
					GROUP BY QuestionID
					HAVING COUNT(AnswerID) >= 4);

----- Question 8: Lấy ra các mã đề thi có thời gian thi >= 60 phút và được tạo trước ngày 20/12/2019 -----
SELECT `Code`
FROM Exam
WHERE Duration >= 60 AND CreateDate < '2019-12-20';

----- Question 9: Lấy ra 5 group được tạo gần đây nhất -----
SELECT *
FROM `Group`
ORDER BY CreateDate DESC
LIMIT 5;

----- Question 10: Đếm số nhân viên thuộc department có id = 2 -----
SELECT COUNT(*)
FROM `Account`
WHERE DepartmentID = 2;

----- Question 11: Lấy ra nhân viên có tên bắt đầu bằng chữ "D" và kết thúc bằng chữ "o" -----
SELECT *
FROM `Account`
WHERE FullName LIKE 'D%' AND FullName LIKE '%o';

----- Question 12: Xóa tất cả các exam được tạo trước ngày 20/12/2019 -----
DELETE FROM Exam
WHERE CreateDate < '2019-12-20';

----- Question 13: Xóa tất cả các question có nội dung bắt đầu bằng từ "câu hỏi" -----
DELETE FROM Question
WHERE Content LIKE 'câu hỏi%';

----- Question 14: Update thông tin của account có id = 5 thành tên "Lô Văn Đề" và email thành lo.vande@mmc.edu.vn -----
UPDATE `Account`
SET 	FullName = N'Lô Văn Đề' AND Email = 'lo.vande@mmc.edu.vn'
WHERE 	AccountID = 5;

----- Question 15: Update account có id = 5 sẽ thuộc group có id = 4 -----
DELETE FROM GroupAccount
WHERE 	AccountID = 5 AND GroupID  = 4;

INSERT INTO `GroupAccount`	(  GroupID	,	AccountID	, JoinDate	 )
VALUES 						(	4		,    5			,'2020-03-28');
                            
