# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Announcement(models.Model):
    an_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    announcement_id = models.IntegerField()
    announcement_title = models.CharField(max_length=64)
    announcement = models.CharField(max_length=256)
    post = models.CharField(max_length=64)
    datetime = models.DateTimeField()
    is_delete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'announcement'


class Attendance(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    job_number = models.CharField(max_length=32)
    name = models.CharField(max_length=64)
    department_id = models.CharField(max_length=64)
    datetime = models.DateTimeField()
    is_leave = models.IntegerField(blank=True, null=True)
    remarks = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attendance'


class AttendanceStatistics(models.Model):
    attend_s_id = models.AutoField(primary_key=True)
    attendance = models.ForeignKey(Attendance, models.DO_NOTHING, blank=True, null=True)
    date = models.DateTimeField()
    department_id = models.IntegerField()
    should_attendance_number = models.IntegerField()
    attendance_number = models.IntegerField()
    leave_number = models.IntegerField()
    statistical_notes = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attendance_statistics'


class Department(models.Model):
    """部门"""
    d_id = models.AutoField(primary_key=True)  # 主键id
    department_num = models.CharField(max_length=32,unique=True)  # 部门编号
    department = models.CharField(max_length=64)  # 部门名称
    higher_id = models.IntegerField()  # 上级部门id
    description = models.CharField(max_length=256, blank=True, null=True)  # 部门描述
    is_delete = models.IntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'department'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class InteriorEmail(models.Model):
    e_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    email_title = models.CharField(max_length=64)
    email_content = models.CharField(max_length=1024)
    sender = models.CharField(max_length=64)
    receiver = models.CharField(max_length=64)
    copyer = models.CharField(max_length=64)
    send_state = models.IntegerField()
    is_delete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'email'


class File(models.Model):
    f_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    file_id = models.CharField(max_length=32)
    job_number = models.CharField(max_length=32)
    name = models.CharField(max_length=64)
    sex = models.IntegerField()
    age = models.IntegerField()
    address = models.CharField(max_length=256)
    phone = models.CharField(max_length=11)
    emp_pwd = models.CharField(max_length=16)
    entry_date = models.DateField()
    brithday = models.DateField()
    department_id = models.IntegerField()
    post = models.CharField(max_length=64)
    work_status = models.CharField(max_length=32)
    is_delete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'file'


class Log(models.Model):
    l_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    log_id = models.IntegerField()
    log = models.CharField(max_length=1024)
    datetime = models.DateTimeField()
    job_number = models.CharField(max_length=32)
    is_delete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'log'


class Meeting(models.Model):
    m_id = models.AutoField(primary_key=True)
    meeting_id = models.IntegerField()
    meeting_room = models.CharField(max_length=64)
    job_number = models.CharField(max_length=32)
    department_id = models.CharField(max_length=11, blank=True, null=True)
    meeting_date = models.DateTimeField()
    meeting_title = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'meeting'


class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)  # 编号
    pid = models.IntegerField(blank=True, null=True)  # 父级编号
    menu_name = models.CharField(max_length=64, blank=True, null=True)  # 菜单名称
    menu_type = models.IntegerField(blank=True, null=True)  # 菜单类型
    menu_level = models.IntegerField(blank=True, null=True)  # 菜单层次级别
    sort = models.IntegerField(blank=True, null=True)  # 排序
    menu_href = models.CharField(max_length=1024, blank=True, null=True)  # 菜单链接
    menu_icon = models.CharField(max_length=100, blank=True, null=True)  # 菜单图标
    permission = models.CharField(max_length=256, blank=True, null=True)  # 权限标识(权限值)
    request_method = models.CharField(max_length=16, blank=True, null=True)  # 请求方法
    request_arguments = models.CharField(max_length=512, blank=True, null=True)  # 请求必带参数
    request_arguments2 = models.CharField(max_length=512, blank=True, null=True)  # 请求必须带有某些值参数
    hook_function = models.CharField(max_length=256, blank=True, null=True)  # 自定义钩子函数
    is_del = models.IntegerField(blank=True, null=True)  # 是否删除
    create_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)  # 创建时间
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True)  # 更改时间

    class Meta:
        managed = False
        db_table = 'menu'


class News(models.Model):
    ne_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    news_id = models.IntegerField()
    news_title = models.CharField(max_length=64)
    news_content = models.TextField()
    post = models.CharField(max_length=64)
    is_delete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'news'


class OfficeGoods(models.Model):
    office_goods_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    goods_id = models.IntegerField()
    goods = models.CharField(max_length=64)
    job_number = models.CharField(max_length=32, blank=True, null=True)
    department_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'office_goods'


class Role(models.Model):
    """角色"""
    role_id = models.AutoField(primary_key=True) # 自增id
    post_id = models.CharField(max_length=64,unique=True) # 角色id
    post = models.CharField(max_length=64) # 角色名
    remark = models.CharField(max_length=256, blank=True, null=True)  # 岗位备注信息
    is_delete = models.IntegerField(default=0)


    class Meta:
        managed = False
        db_table = 'role'


class RoleMenu(models.Model):
    role = models.ForeignKey(Role, models.DO_NOTHING, primary_key=True)
    menu = models.ForeignKey(Menu, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'role_menu'
        unique_together = (('role', 'menu'),)


class Salary(models.Model):
    s_id = models.AutoField(primary_key=True)                                       # 自增字段
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)     # 关联到用户表
    salary_id = models.IntegerField()                                                # 薪水ID
    time = models.DateField()                                                        # 工资当发时间
    job_number = models.CharField(max_length=32)                                     # 员工编号
    name = models.CharField(max_length=64)                                           # 员工姓名
    basic_salary = models.FloatField()                                               # 基础薪资
    deduct_salary = models.FloatField()                                              # 应扣工资
    allowance = models.FloatField()                                                  # 津贴
    award = models.FloatField()                                                      # 奖金
    five_insurance = models.FloatField()                                             # 五险
    provident_fund = models.FloatField()                                             # 公积金
    real_salary = models.FloatField()                                                # 实际工资
    salary_status = models.Field(choices=((1, '未发放'), (2, '已发放'),),
                                 default='未发放')                                              # 工资发放状态

    class Meta:
        managed = False
        db_table = 'salary'

    def to_dict(self):
        """转化为字典可以给前端传"""
        user = User.objects.filter(job_number=self.job_number).first()
        return {
            'jobNumber': self.job_number,
            'time': self.time,
            'userName': self.name,
            'staff_department': user.department,
            'basic_salary': self.basic_salary,
            'deduct_salary': self.deduct_salary,
            'allowance': self.allowance,
            'award': self.award,
            'five_insurance': self.five_insurance,
            'provident_fund': self.provident_fund,
            'real_salary': self.real_salary,
            'salary_status': self.salary_status,
        }


class User(models.Model):
    user_id = models.AutoField(primary_key=True)  # 用户id
    m = models.ForeignKey(Meeting, models.DO_NOTHING, blank=True, null=True) # 会议id
    d = models.ForeignKey(Department, models.DO_NOTHING, blank=True, null=True) # 部门id
    sex = models.IntegerField(default=1) #  用户性别,1默认为男
    job_number = models.CharField(max_length=32,unique=True)  # 工号
    name = models.CharField(max_length=64)  # 姓名
    phone = models.CharField(max_length=11)  # 联系电话
    email = models.CharField(max_length=32)  # 邮箱
    office_phone = models.CharField(max_length=20, blank=True, null=True)  # 办公电话
    password = models.CharField(max_length=32)
    role = models.ManyToManyField(Role, through='UserRole')  # 用户角色
    is_delete = models.IntegerField(default=0)  # 默认不删除信息


    class Meta:
        managed = False
        db_table = 'user'


class UserRole(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    role = models.ForeignKey(Role, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_role'
        unique_together = (('user', 'role'),)
