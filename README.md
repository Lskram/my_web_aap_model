# 💾 การนำโปรเจค My Web Application ขึ้นไปบน repmote repo บน github


## 🧠 &larr; ความรู้ที่ได้รับ


### 🎯 1. การโคลนโปรเจ็คเริ่มต้นมาใส่ใน Repository โดยการเซ็ต Remote ใหม่โดยใช้คำสั่งโค๊ดว่า **git clone** 
```shell
> git clone <url>
```
## ⚙คำสั่งเปลี่ยนชื่อไฟล์
```shell
> rename-item Project2565 Project2566
```
- [x] สามารถเข้าใจได้
- [ ] ยังไม่ค่อยเข้าใจ
- [ ] ไม่เข้าใจเลย

      
### 🎯 2. การเซ็ต Remote Repository ภายใต้คำสั่ง **git remote set-url origin**
```shell
> git remote set-url origin <url>
```
- [x] สามารถเข้าใจได้
- [ ] ยังไม่ค่อยเข้าใจ
- [ ] ไม่เข้าใจเลย


### 🎯 3. การเช็คสถานะว่า Remote ชี้ไปที่ Repository ไหนภายใต้คำสั่งโค๊ด **git remote -v**
```shell
> git remote -v
```
- [x] สามารถเข้าใจได้
- [ ] ยังไม่ค่อยเข้าใจ
- [ ] ไม่เข้าใจเลย

      
### 🎯 4. การสร้างตาราง และ การใช้ Prefix Choices
```shell
        > prefix_choices =(
            (1,"นาย"),
            (2,"นางสาว"),
            (3,"นาง"),
        )
        
        class Student(models.Model):
            std_id =    models.IntegerField()
            prefix = models.IntegerField(choices=prefix_choices,    default=1)
            name=       models.CharField(max_length=255)
            lastname=   models.CharField(max_length=255)
            phone =     models.CharField(max_length=255)
            address=    models.TextField()
            
        
            class Meta:
                verbose_name = 'student'
                verbose_name_plural = 'student'
        
            def __str__(self):
                return self.name + " " + self.lastname
        
```
- [ ] สามารถเข้าใจได้
- [x] ยังไม่ค่อยเข้าใจ
- [ ] ไม่เข้าใจเลย


### 🎯 5. การดึงข้อมูลมาแสดงในหน้า Model โดยขั้นตอนที่ 1 Import Models ในหน้า Views
```shell
>from . import models
```
#### ภาพประกอบ🖼
![image](https://github.com/Lskram/my_web_aap_model/blob/main/immage/import.png)
- [x] สามารถเข้าใจได้
- [ ] ยังไม่ค่อยเข้าใจ
- [ ] ไม่เข้าใจเลย


### 🎯 6. การเรียงลำดับด้วยตัวแปรยกตัวอย่างเลขนักศึกษา เช่น
#### ⌨ Views  &rarr; Def Home และใช้ .order_by("std_id") ดังนี้
```shell
>students = models.Student.objects.all().order_by("std_id")
```
- [x] สามารถเข้าใจได้
- [ ] ยังไม่ค่อยเข้าใจ
- [ ] ไม่เข้าใจเลย


### 🎯 7. การสร้าง Class Student ข้อมูลนักศึกษา 
#### โดยการสร้างฟังก์ชั่น Details ใน Views.py
```shell
>class  Student(models.Model):

	std_id  =  models.IntegerField()

	prefix  =  models.IntegerField(choices=prefix_choices, default=1)

	name  =  models.CharField(max_length=255)

	lastname  =  models.CharField(max_length=255)

	phone  =  models.CharField(max_length=15)

	address  =  models.TextField()


	class  Meta:

	verbose_name  =  "Student"

	verbose_name_plural  =  "Students"


	def  __str__(self):

	return  self.name


	def  get_absolute_url(self):

	return  reversed("Student_detail", kwargs={"pk": self.pk})
```
- [x] สามารถเข้าใจได้
- [ ] ยังไม่ค่อยเข้าใจ
- [ ] ไม่เข้าใจเลย


### 🎯 8. การสร้าง Class Major ข้อมูลของคณะนักศึกษา
```shell
>class Major(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Major"
        verbose_name_plural = "Majors"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reversed("Major_detail", kwargs={"pk": self.pk})
```
- [x] สามารถเข้าใจได้
- [ ] ยังไม่ค่อยเข้าใจ
- [ ] ไม่เข้าใจเลย


### 🎯 9. การใช้คำสั่ง makemigrations และ migrate เพื่อสร้างฐานข้อมูล
ใช้คำสั่ง makemigrations และ migrate เพื่อสร้างฐานข้อมูล แล้วจึงใช้คำสั่ง createsuperuser เพื่อสร้าง admin user ในการเข้าถึงฐานข้อมูล
> :warning: **Warning:**  หลังจากการสร้างหรือปรับเปลี่ยนตารางสำหรับการเก็บข้อมูลใหม่ทุกครั้งๆจำเป็นจะต้องใช้คำสั่งดังกล่าวเพื่อสร้างฐานข้อมูลใหม่ด้วยเช่นกัน
```sh
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
- [x] สามารถเข้าใจได้
- [ ] ยังไม่ค่อยเข้าใจ
- [ ] ไม่เข้าใจเลย

      
## รูปภาพประกอบการเรียนรู้ 📂


### การเพิ่มข้อมูล Student 🌈
![image](https://github.com/Lskram/my_web_aap_model/blob/main/immage/1.png)
#### 🛠 สามารถเพิ่มข้อมูลนักศึกษาจากระบบหลังบ้านได้ทุกเวลาจากระบบหลังบ้าน
- [x] สามารถเข้าใจได้
- [ ] ยังไม่ค่อยเข้าใจ
- [ ] ไม่เข้าใจเลย


### การเพิ่ม Major 🌈
![image](https://github.com/Lskram/my_web_aap_model/blob/main/immage/Major.png)
#### 🛠 สามารถเพิ่มข้อมูลคณะนักศึกษาจากระบบหลังบ้านได้ทุกเวลาจากระบบหลังบ้าน
- [x] สามารถเข้าใจได้
- [ ] ยังไม่ค่อยเข้าใจ
- [ ] ไม่เข้าใจเลย
      
### สำหรับทำความเข้าใจความสัมพันธ์แบบ One-to-Many🌈
### ความสัมพันธ์แบบ One-to-Many คือความสัมพันธ์ระหว่างสองตารางที่ตารางหนึ่งมีข้อมูลหนึ่งรายการและตารางที่สองมีข้อมูลหลายรายการที่เกี่ยวข้องกัน ตัวอย่างเช่น ตาราง customers อาจมีข้อมูลลูกค้าหนึ่งรายการและตาราง orders อาจมีข้อมูลหลายรายการที่สั่งซื้อโดยลูกค้าคนนั้น
Django ช่วยให้สร้างแอปพลิเคชันที่จัดการความสัมพันธ์แบบ One-to-Many ได้โดยใช้ ForeignKey ฟิลด์ในโมเดล ฟิลด์ ForeignKey ระบุความสัมพันธ์ระหว่างโมเดลสองโมเดล โดยระบุว่าโมเดลหนึ่ง (โมเดลหลัก) มีความสัมพันธ์กับโมเดลอื่น (โมเดลรอง)
## รูปภาพประกอบการเรียนรู้ 📂
![image](https://github.com/Lskram/News/blob/main/media/content/%E0%B9%83%E0%B8%AA%E0%B9%88%E0%B9%80%E0%B8%99%E0%B8%B7%E0%B9%89%E0%B8%AD%E0%B8%AB%E0%B8%B2%E0%B8%82%E0%B9%88%E0%B8%B2%E0%B8%A7.png)
![image](https://github.com/Lskram/News/blob/main/media/content/%E0%B9%80%E0%B8%99%E0%B8%B7%E0%B9%89%E0%B8%AD%E0%B8%AB%E0%B8%B2%E0%B8%82%E0%B9%88%E0%B8%B2%E0%B8%A7%202.png)
- [ ] สามารถเข้าใจได้
- [x] ยังไม่ค่อยเข้าใจ
- [ ] ไม่เข้าใจเลย
