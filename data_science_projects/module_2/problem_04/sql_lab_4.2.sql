USE Testing_System_Db;

----- Exercise 1: Join -----
----- Question 1: Viết lệnh để lấy ra danh sách nhân viên và thông tin phòng ban của họ -----
SELECT  `Account`.*, Department.*
FROM 	`Account` INNER JOIN Department 
ON 		`Account`.DepartmentID = Department.DepartmentID;

----- Question 2: Viết lệnh để lấy ra thông tin các account được tạo sau ngày 20/12/2010 -----
SELECT *
FROM 	`Account`
WHERE   CreateDate > '2010-12-20';

----- Question 3: Viết lệnh để lấy ra tất cả các developer -----
SELECT  *
FROM 	`Account` INNER JOIN GroupAccount
ON   	`Account`.AccountID = GroupAccount.AccountID
WHERE 	GroupAccount.AccountID = (SELECT GroupID
								 FROM `Group`
								 WHERE GroupName = N'Development');
                                 
----- Question 4: Viết lệnh để lấy ra danh sách các phòng ban có >3 nhân viên -----
SELECT 		Department.*
FROM 		`Account` INNER JOIN Department
ON   		`Account`.DepartmentID = Department.DepartmentID
GROUP BY 	DepartmentID
HAVING 		COUNT(`Account`.AccountID)>3;

----- Question 5: Viết lệnh để lấy ra danh sách câu hỏi được sử dụng trong đề thi nhiều nhất -----
SELECT  Question.*
FROM 	ExamQuestion INNER JOIN Question
ON      ExamQuestion.QuestionID = Question.QuestionID
GROUP BY ExamQuestion.QuestionID
HAVING   COUNT(ExamQuestion.ExamID) =   (SELECT COUNT(ExamID)
										FROM 	ExamQuestion
										GROUP BY QuestionID
										ORDER BY COUNT(ExamID) DESC
										LIMIT 1);

----- Question 6: Thống kê mỗi category Question được sử dụng trong bao nhiêu Question -----
SELECT 		CategoryQuestion.CategoryName, COUNT(Question.QuestionID) AS NUM_QUESTIONS
FROM  		Question INNER JOIN CategoryQuestion
ON 			Question.CategoryID = CategoryQuestion.CategoryID
GROUP BY 	Question.CategoryID;

----- Question 7: Thông kê mỗi Question được sử dụng trong bao nhiêu Exam -----
SELECT 		Question.QuestionID, COUNT(ExamQuestion.ExamID) AS NUM_EXAMS
FROM 		ExamQuestion INNER JOIN Question
ON      	ExamQuestion.QuestionID = Question.QuestionID
GROUP BY 	ExamQuestion.QuestionID;

----- Question 8: Lấy ra Question có nhiều câu trả lời nhất -----
SELECT  Question.*
FROM 	Answer INNER JOIN Question
ON      Answer.QuestionID = Question.QuestionID
GROUP BY Answer.QuestionID
HAVING   COUNT(Answer.AnswerID) =   (SELECT  COUNT(AnswerID)
									FROM 	 Answer
									GROUP BY QuestionID
									ORDER BY COUNT(AnswerID) DESC
									LIMIT 1);

----- Question 9: Thống kê số lượng account trong mỗi group -----
SELECT 		GroupAccount.GroupID, COUNT(GroupAccount.AccountID) AS NUM_ACCOUNTS
FROM 		GroupAccount INNER JOIN `Account`
ON      	GroupAccount.AccountID = `Account`.AccountID
GROUP BY 	GroupAccount.GroupID;

----- Question 10: Tìm chức vụ có ít người nhất -----
SELECT  `Position`.*
FROM 	`Account` INNER JOIN `Position`
ON      `Account`.PositionID = `Position`.PositionID
GROUP BY `Account`.PositionID
HAVING   COUNT(`Account`.AccountID) =   (SELECT  COUNT(AccountID)
										FROM 	 `Account`
										GROUP BY PositionID
										ORDER BY COUNT(AccountID)
										LIMIT 1);

----- Question 11: Thống kê mỗi phòng ban có bao nhiêu dev, test, scrum master, PM -----
SELECT   Department.DepartmentName, `Position`.PositionName, COUNT(`Position`.PositionID)
FROM 	`Account` INNER JOIN `Position`
ON      `Account`.PositionID = `Position`.PositionID
INNER JOIN Department
ON      `Account`.DepartmentID = Department.DepartmentID
GROUP BY  `Account`.DepartmentID, `Position`.PositionID;

----- Question 12: Lấy thông tin chi tiết của câu hỏi bao gồm: thông tin cơ bản của question, loại câu hỏi, ai là người tạo ra câu hỏi, câu trả lời là gì,… -----
SELECT 	Question.*, TypeQuestion.TypeName, `Account`.FullName, Answer.Content AS 'ANSWER'
FROM 	Answer INNER JOIN Question
ON      Answer.QuestionID = Question.QuestionID 
INNER JOIN TypeQuestion
ON      Question.TypeID = TypeQuestion.TypeID
INNER JOIN `Account`
ON      `Account`.AccountID = Question.CreatorID;

----- Question 13: Lấy ra số lượng câu hỏi của mỗi loại tự luận hay trắc nghiệm -----
SELECT 		TypeQuestion.TypeName, COUNT(Question.QuestionID) AS NUM_QUESTIONS
FROM 		Question INNER JOIN TypeQuestion
ON      	Question.TypeID = TypeQuestion.TypeID
GROUP BY 	Question.TypeID;
----- Question 14: Lấy ra group không có account nào -----
SELECT `Group`.*
FROM  `Group`
WHERE GroupID NOT IN (SELECT GroupID
					 FROM  GroupAccount);

----- Question 15: Lấy ra group không có account nào -----
SELECT `Group`.*
FROM  `Group`
WHERE GroupID NOT IN (SELECT GroupID
					 FROM  GroupAccount);
                     
----- Question 16: Lấy ra question không có answer nào -----
SELECT Question.*
FROM  Question
WHERE Question.QuestionID NOT IN (SELECT QuestionID
								 FROM  Answer);
                                 
----- Exercise 2: Union -----
----- Question 17: -----
----- a) Lấy các account thuộc nhóm thứ 1 -----
SELECT  `Account`.*
FROM 	`Account` INNER JOIN GroupAccount
ON      `Account`.AccountID = GroupAccount.AccountID
WHERE   GroupAccount.GroupID = 1; 
----- b) Lấy các account thuộc nhóm thứ 2 -----
SELECT  `Account`.*
FROM 	`Account` INNER JOIN GroupAccount
ON      `Account`.AccountID = GroupAccount.AccountID
WHERE   GroupAccount.GroupID = 2; 
----- c) Ghép 2 kết quả từ câu a) và câu b) sao cho không có record nào trùng nhau -----
SELECT  `Account`.*
FROM 	`Account` INNER JOIN GroupAccount
ON      `Account`.AccountID = GroupAccount.AccountID
WHERE   GroupAccount.GroupID = 1
UNION
SELECT  `Account`.*
FROM 	`Account` INNER JOIN GroupAccount
ON      `Account`.AccountID = GroupAccount.AccountID
WHERE   GroupAccount.GroupID = 2; 
----- Question 18: -----
----- a) Lấy các group có lớn hơn 5 thành viên -----
SELECT 		`Group`.*
FROM		GroupAccount INNER JOIN `Group`
ON      	GroupAccount.GroupID = `Group`.GroupID
GROUP BY 	GroupAccount.GroupID
HAVING		COUNT(GroupAccount.AccountID) > 5;
----- b) Lấy các group có nhỏ hơn 7 thành viên -----
SELECT 		`Group`.*
FROM		GroupAccount INNER JOIN `Group`
ON      	GroupAccount.GroupID = `Group`.GroupID
GROUP BY 	GroupAccount.GroupID
HAVING		COUNT(GroupAccount.AccountID) > 7;
----- c) Ghép 2 kết quả từ câu a) và câu b) -----
SELECT 		`Group`.*
FROM		GroupAccount INNER JOIN `Group`
ON      	GroupAccount.GroupID = `Group`.GroupID
GROUP BY 	GroupAccount.GroupID
HAVING		COUNT(GroupAccount.AccountID) > 5
UNION ALL
SELECT 		`Group`.*
FROM		GroupAccount INNER JOIN `Group`
ON      	GroupAccount.GroupID = `Group`.GroupID
GROUP BY 	GroupAccount.GroupID
HAVING		COUNT(GroupAccount.AccountID) > 7;