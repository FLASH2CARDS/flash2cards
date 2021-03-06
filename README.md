## FLASH2CARDS

---

###  Table of Contents 

- [Getting started](#Getting-started)
- [App features](#App-features)
- [Used technologies](#Used-technologies)
- [How to run tests](#How-to-run-tests)
- [TODO](#TODO)
- [Authors](#Authors)

---

Web app for learning any subject with flashcards created by user. 
The one of the most powerful systems to memorize smaller or bigger knowledge areas.
In this flashcards universe registered user can: 
- search flashcards by demanded subjects, 
- use flashcards sets prepared by others,
- create own cards and collect them into subject sets,
- share own cards with others or keep them private,

... and the most important 

#### LEARN, LEARN and LEARN it easy everywhere!

---

### Getting started

Clone the repository:

``` 
git clone https://github.com/FLASH2CARDS/flash2cards.git
```

Add a virtual environment in the project root and activate it:
```
python3 -m venv venv
source venv/bin/activate
```

Install all dependencies separately, or all at once from the file:

``` 
pip install -r requirements.txt
```

Run development server:

```
python manage.py runserver
```

[Back to the Top ^](#FLASH2CARDS)

---
### App features

Separate access for **_registered_** and **_unregistered_** user.

> **Unregistered user** can:
>- search flashcards by categories / subjects / words,
>- search flashcards by key-words,
>- study chosen flashcards set without progress saving.


> **Registered user** can:
>- search flashcards by categories / subjects / words,
>- search flashcards by key-words,
>- create and edit own flashcards,
>- create and edit own flashcards sets,
>- set flashcards / sets status to private or public
>- comment and rate others single flashcards and others sets,
>- study chosen flashcards set with preferred settings,
>- follow up the progress statistics, 
>- export flashcards to txt/csv file, 
>- import flashcards from txt/csv file.

> **Learning mode**:
>>- **unregistered user** can run the mode without settings,
>
>>- **registered user** can run learning mode and set:
>>  - flashcards amount per learning session,
>>  - study time per learning session,
>>  - flashcards display order [ordered / random],
>>  - one or more category sets.

>**Admin** panel:
>- manage flashcards / sets like registered user,
>- manage categories,
>- manage users (grant users with higher rates),
>- set achievements grant system for high activity.

[Back to the Top ^](#FLASH2CARDS)


---
### Used technologies

- Python 3.8
- Django 3.2
- django-ckeditor 6.0
- python-dotenv 0.17
- django-mptt 0.12.0
- django-tinymce
- mySQL (mysqlclient 2.0.3)
- unittest
- pytest 6.2
- pytest-django
- JSON



[Back to the Top ^](#FLASH2CARDS)

---

### How to run tests

- unittest
  
```
./python -m -v <test_file_name>
```
  
- pytest 
  
```
./pytest -v <test_file_name>
```

[Back to the Top ^](#FLASH2CARDS)

---

### TODO

... really, a lot to do :)

Progress:

> First sprint started

[Back to the Top ^](#FLASH2CARDS)

---
### Authors

- Przemek Hinca / GitHub: [pshemekhinca](https://github.com/pshemekhinca)
- Micha?? Przychodzie?? / GitHub: [MichalPrzychodzien](https://github.com/MichalPrzychodzien)


[Back to the Top ^](#FLASH2CARDS)

