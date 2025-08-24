from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Subject, Commendation
from random import choice
from django.core.exceptions import ObjectDoesNotExitst, MultipleObjectsReturned


COMPLIMENTS = [
        "Молодец!",
        "Отлично!",
        "Хорошо!",
        "Гораздо лучше, чем я ожидал!",
        "Ты меня приятно удивил!",
        "Великолепно!",
        "Прекрасно!",
        "Ты меня очень обрадовал!",
        "Именно этого я давно ждал от тебя!",
        "Сказано здорово – просто и ясно!",
        "Ты, как всегда, точен!",
        "Очень хороший ответ!",
        "Талантливо!",
        "Ты сегодня прыгнул выше головы!",
        "Я поражен!",
        "Уже существенно лучше!",
        "Потрясающе!",
        "Замечательно!",
        "Прекрасное начало!",
        "Так держать!",
        "Ты на верном пути!",
        "Здорово!",
        "Это как раз то, что нужно!",
        "Я тобой горжусь!",
        "С каждым разом у тебя получается всё лучше!",
        "Мы с тобой не зря поработали!",
        "Я вижу, как ты стараешься!",
        "Ты растешь над собой!",
        "Ты многое сделал, я это вижу!",
        "Теперь у тебя точно все получится!"
    ]


def get_pupil_by_name(name: str):
    try:
        return Schoolkid.objects.get(full_name__contains=name)
    except ObjectDoesNotExitst:
        print("Такого ученика нет в базе")
    except MultipleObjectsReturned:
        print("Найдено больше, чем 1 ученик с такими данными!")


def fix_marks(schoolkid: str):
    pupil = get_pupil_by_name(schoolkid)
    bad_marks = Mark.objects.filter(schoolkid=pupil, points__in=[2,3])
    bad_marks.update(points=5)


def remove_chastisements(schoolkid: str):
    pupil = get_pupil_by_name(schoolkid)
    chasitsements = Chastisement.objects.filter(schoolkid=pupil)
    chasitsements.delete()


def create_commendation(schoolkid: str, subject: str, compliments: list):
    pupil = get_pupil_by_name(schoolkid)
    try:
        subj = Subject.objects.get(title__contains=subject, year_of_study=pupil.year_of_study)
        lesson = choice(Lesson.objects.filter(year_of_study=pupil.year_of_study, group_letter=pupil.group_letter, subject=subj).order_by("date"))
    except ObjectDoesNotExitst:
        print("Такого урока не существует")
    commendation_text = choice(compliments)
    Commendation.objects.create(text=commendation_text, created=lesson.date, schoolkid=pupil, subject=subj, teacher=lesson.teacher)