from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Subject
from random import choice

def get_pupil_by_name(name: str):
    return Schoolkid.objects.get(full_name__contains=name)


def fix_marks(schoolkid: str):
    pupil = get_pupil_by_name(schoolkid)
    bad_marks = Mark.objects.filter(schoolkid=pupil, points__in=[2,3])
    bad_marks.update(points=5)


def remove_chastisements(schoolkid: str):
    pupil = get_pupil_by_name(schoolkid)
    chasitsements = Chastisement.objects.filter(schoolkid=name)
    chasitsements.delete()


def create_commendation(schoolkid: str, subject: str):
    phrases = [
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
    pupil = get_pupil_by_name(schoolkid)
    subj = Subject.objects.get(title__contains=subject, year_of_study=pupil.year_of_study)
    lesson = choice(Lesson.objects.filter(year_of_study=pupil.year_of_study, group_letter=pupil.group_letter, subject=subj))
    commendation_text = choice(phrases)
    Commendation.objects.create(text=commendation_text, created=lesson.date, schoolkid=pupil, subject=subj, teacher=lesson.teacher)