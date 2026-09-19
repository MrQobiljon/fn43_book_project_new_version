from django.shortcuts import render, redirect
from .models import Category, Book

categories = [
    "Badiiy adabiyot",
    "Ilmiy-ommabop kitoblar",
    "Dasturlash",
    "Biznes va tadbirkorlik",
    "Psixologiya",
    "Tarix",
    "Bolalar adabiyoti",
    "Chet tillari",
    "Shaxsiy rivojlanish",
    "Diniy adabiyot",
]


books = [
    {
        "title": "O‘tkan kunlar",
        "introduction": "Abdulla Qodiriyning o‘zbek adabiyotidagi mashhur tarixiy romani.",
        "price": 45000,
        "published": True,
        "category": "Badiiy adabiyot",
    },
    {
        "title": "Mehrobdan chayon",
        "introduction": "Abdulla Qodiriyning tarixiy va ijtimoiy mavzudagi mashhur asari.",
        "price": 42000,
        "published": True,
        "category": "Badiiy adabiyot",
    },
    {
        "title": "Kecha va kunduz",
        "introduction": "Cho‘lpon qalamiga mansub o‘zbek adabiyotining muhim romanlaridan biri.",
        "price": 48000,
        "published": True,
        "category": "Badiiy adabiyot",
    },
    {
        "title": "Ikki eshik orasi",
        "introduction": "O‘tkir Hoshimovning insoniy munosabatlar va hayot haqida yozilgan mashhur romani.",
        "price": 55000,
        "published": True,
        "category": "Badiiy adabiyot",
    },
    {
        "title": "Dunyoning ishlari",
        "introduction": "Ona, oila va insoniy qadriyatlar haqida hikoya qiluvchi asar.",
        "price": 39000,
        "published": True,
        "category": "Badiiy adabiyot",
    },

    {
        "title": "Python dasturlash asoslari",
        "introduction": "Python dasturlash tilini boshlang‘ich darajadan o‘rganish uchun qo‘llanma.",
        "price": 85000,
        "published": True,
        "category": "Dasturlash",
    },
    {
        "title": "Python Backend dasturlash",
        "introduction": "Python yordamida backend dasturlashni o‘rganish uchun amaliy qo‘llanma.",
        "price": 120000,
        "published": True,
        "category": "Dasturlash",
    },
    {
        "title": "Django bilan web dasturlash",
        "introduction": "Django framework yordamida zamonaviy web ilovalar yaratish.",
        "price": 110000,
        "published": True,
        "category": "Dasturlash",
    },
    {
        "title": "JavaScript asoslari",
        "introduction": "JavaScript dasturlash tilining asosiy tushunchalari va amaliy misollar.",
        "price": 75000,
        "published": True,
        "category": "Dasturlash",
    },
    {
        "title": "Algoritmlar va ma’lumotlar tuzilmalari",
        "introduction": "Algoritmlar, massivlar, bog‘langan ro‘yxatlar, steklar va navbatlar.",
        "price": 95000,
        "published": True,
        "category": "Dasturlash",
    },

    {
        "title": "Boy ota, kambag‘al ota",
        "introduction": "Moliyaviy savodxonlik va shaxsiy moliyani boshqarish haqida kitob.",
        "price": 65000,
        "published": True,
        "category": "Biznes va tadbirkorlik",
    },
    {
        "title": "Biznes boshlash asoslari",
        "introduction": "Biznes g‘oya yaratish va uni amaliyotga tatbiq qilish bo‘yicha qo‘llanma.",
        "price": 70000,
        "published": True,
        "category": "Biznes va tadbirkorlik",
    },
    {
        "title": "Marketing asoslari",
        "introduction": "Marketing strategiyalari, mijozlar va bozorni o‘rganish haqida.",
        "price": 80000,
        "published": True,
        "category": "Biznes va tadbirkorlik",
    },

    {
        "title": "Inson bo‘lish san’ati",
        "introduction": "Insonning o‘zini anglash va hayotdagi munosabatlari haqida.",
        "price": 58000,
        "published": True,
        "category": "Psixologiya",
    },
    {
        "title": "O‘z-o‘zini rivojlantirish",
        "introduction": "Maqsad qo‘yish, vaqtni boshqarish va foydali odatlarni shakllantirish.",
        "price": 62000,
        "published": True,
        "category": "Psixologiya",
    },
    {
        "title": "Muloqot psixologiyasi",
        "introduction": "Odamlar bilan samarali muloqot qilish va munosabatlarni yaxshilash.",
        "price": 68000,
        "published": True,
        "category": "Psixologiya",
    },

    {
        "title": "O‘zbekiston tarixi",
        "introduction": "O‘zbekiston hududidagi qadimgi davrlardan zamonaviy davrgacha bo‘lgan tarix.",
        "price": 90000,
        "published": True,
        "category": "Tarix",
    },
    {
        "title": "Buyuk ipak yo‘li",
        "introduction": "Buyuk ipak yo‘lining Markaziy Osiyo tarixidagi o‘rni haqida.",
        "price": 72000,
        "published": True,
        "category": "Tarix",
    },
    {
        "title": "Temuriylar davri",
        "introduction": "Amir Temur va Temuriylar davri tarixi haqida ma’lumotlar.",
        "price": 85000,
        "published": True,
        "category": "Tarix",
    },

    {
        "title": "Bolalar uchun ertaklar",
        "introduction": "Bolalar uchun qiziqarli va tarbiyaviy ertaklar to‘plami.",
        "price": 35000,
        "published": True,
        "category": "Bolalar adabiyoti",
    },
    {
        "title": "Sehrli dunyo",
        "introduction": "Bolalar tasavvurini rivojlantirishga yordam beradigan qiziqarli hikoyalar.",
        "price": 40000,
        "published": True,
        "category": "Bolalar adabiyoti",
    },
    {
        "title": "Aqlli bolalar uchun 100 savol",
        "introduction": "Bolalarning bilimini oshirish uchun qiziqarli savol va topshiriqlar.",
        "price": 45000,
        "published": True,
        "category": "Bolalar adabiyoti",
    },

    {
        "title": "Ingliz tili Beginner",
        "introduction": "Ingliz tilini boshlang‘ich darajada o‘rganish uchun qo‘llanma.",
        "price": 60000,
        "published": True,
        "category": "Chet tillari",
    },
    {
        "title": "Ingliz tili grammatikasi",
        "introduction": "Ingliz tili grammatikasining asosiy qoidalari va mashqlari.",
        "price": 75000,
        "published": True,
        "category": "Chet tillari",
    },
    {
        "title": "Inglizcha 5000 so‘z",
        "introduction": "Ingliz tilida eng ko‘p ishlatiladigan so‘zlarni o‘rganish uchun lug‘at.",
        "price": 55000,
        "published": True,
        "category": "Chet tillari",
    },

    {
        "title": "Atom odatlar",
        "introduction": "Kichik odatlar orqali katta natijalarga erishish haqida.",
        "price": 78000,
        "published": True,
        "category": "Shaxsiy rivojlanish",
    },
    {
        "title": "Vaqtni boshqarish",
        "introduction": "Vaqtdan samarali foydalanish va kunni to‘g‘ri rejalashtirish.",
        "price": 60000,
        "published": True,
        "category": "Shaxsiy rivojlanish",
    },
    {
        "title": "Maqsad sari",
        "introduction": "Maqsadlarni belgilash va ularga bosqichma-bosqich erishish haqida.",
        "price": 52000,
        "published": True,
        "category": "Shaxsiy rivojlanish",
    },

    {
        "title": "Qur’on ma’nolari tarjimasi",
        "introduction": "Qur’on oyatlarining o‘zbek tilidagi ma’nolari.",
        "price": 95000,
        "published": True,
        "category": "Diniy adabiyot",
    },
    {
        "title": "Hadislar to‘plami",
        "introduction": "Hadislar va ularning mazmuniga bag‘ishlangan to‘plam.",
        "price": 85000,
        "published": True,
        "category": "Diniy adabiyot",
    },

    # Test uchun published=False bo'lgan kitoblar
    {
        "title": "Yangi Python kitobi",
        "introduction": "Hali saytga chiqarilmagan yangi Python kitobi.",
        "price": 130000,
        "published": False,
        "category": "Dasturlash",
    },
    {
        "title": "Kelajak biznesi",
        "introduction": "Hali nashr jarayonidagi biznes kitobi.",
        "price": 90000,
        "published": False,
        "category": "Biznes va tadbirkorlik",
    },
]


def book_test(request):

    if not Category.objects.all().exists():
        categories_list = []
        for category in categories:
            categories_list.append(Category(name=category))
        Category.objects.bulk_create(categories_list)

    if not Book.objects.all().exists():
        books_list = []
        for book in books:
            books_list.append(
                Book(
                    title=book.get('title'),
                    introduction=book.get('introduction'),
                    price=book.get('price'),
                    published=book.get('published'),
                    category=Category.objects.get(name=book.get('category'))
                )
            )

        Book.objects.bulk_create(books_list)

    return redirect('all_books')
