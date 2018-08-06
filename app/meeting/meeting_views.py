from django.http import JsonResponse
from django.shortcuts import render

from app.models import Meeting, Department, User


def my_meeting(request):
    """
    显示会议页面
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'meeting/my_meeting.html')

def meeting_list(request):
    if request.method == 'GET':
        # meeting_list = Meeting.objects.filter(job_number=1)
        meeting_list = Meeting.objects.all()
        my_list = []
        msg = {
            "code": 0,
            "msg": "",
            "count": len(meeting_list),
        }
        for meeting in meeting_list:
            temp = dict()
            # 会议主题
            temp['meeting_title'] = meeting.meeting_title
            # 会议室
            temp['meeting_room'] = meeting.meeting_room
            # 时间
            temp['meeting_date'] = meeting.meeting_date
            # 参会人员
            if meeting.department_id:
                temp['people'] = Department.objects.get(department_num=meeting.department_id).department
            else:

                temp['people'] = User.objects.get(job_number=meeting.job_number).name
            my_list.append(temp)

        msg['data'] = my_list
        return JsonResponse(msg)


def meeting_appointment(request):
    """
    会议预约
    :param request:
    :return:
    """
    if request.method == 'GET':
        department_id = request.GET.get('department_id')
        department = Department.objects.all()
        if department_id:
            user = User.objects.filter(department_id=department_id)
        else:
            user = User.objects.all()
        data = {
            'department': department,
            'user': user
        }
        return render(request, 'meeting/meeting_appointment.html', {'data': data})
    if request.method == 'POST':
        msg = {
            'code': 0,
            'msg': '请求成功'
        }
        data = request.POST.dict()
        meeting = Meeting()
        meeting.meeting_id = data.get('meeting_id')
        meeting.meeting_room = data.get('meeting_room')
        meeting.meeting_title = data.get('meeting_title')
        meeting.meeting_date = data.get('meeting_date')
        meeting.department_id = data.get('department_id')
        meeting.job_number = data.get('job_number')
        meeting.save()
        return JsonResponse(msg)