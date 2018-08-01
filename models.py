# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

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
    d_id = models.AutoField(primary_key=True)
    department_id = models.IntegerField()
    department = models.CharField(max_length=64)
    higher_id = models.IntegerField()
    description = models.CharField(max_length=256, blank=True, null=True)

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


class Email(models.Model):
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
    department_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meeting'





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
    role_id = models.AutoField(primary_key=True)
    post_id = models.IntegerField()
    post = models.CharField(max_length=64)

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
    s_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    salary_id = models.IntegerField()
    jon_number = models.CharField(max_length=32)
    name = models.CharField(max_length=64)
    basic_salary = models.FloatField()
    deduct_salary = models.FloatField()
    allowance = models.FloatField()
    award = models.FloatField()
    five_insurance = models.FloatField()
    provident_fund = models.FloatField()
    real_salary = models.FloatField()

    class Meta:
        managed = False
        db_table = 'salary'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    m = models.ForeignKey(Meeting, models.DO_NOTHING, blank=True, null=True)
    d = models.ForeignKey(Department, models.DO_NOTHING, blank=True, null=True)
    job_number = models.CharField(max_length=32)
    name = models.CharField(max_length=64)
    department = models.CharField(max_length=64)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=32)
    office_phone = models.CharField(max_length=20, blank=True, null=True)
    post = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'user'


class UserRole(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, primary_key=True)
    role = models.ForeignKey(Role, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_role'
        unique_together = (('user', 'role'),)
