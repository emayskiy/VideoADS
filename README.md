# VideoADS
Добавление рекламного ролика во все видеофайлы из указанного каталога. Для обработки видео используется бибилиотека moviepy. 

## Зависимости
Для работы скрипта требуется установленный python3 и модули moviepy, pillow. 
```
sudo pip3 install moviepy pillow
```

## Описание настроек
* promofile - Файл промовидео который будет добавлен во все видеофайлы
* promointerval - Интервал, через который будет добавлен промо
* srcdir - Каталог в котором распологаются видеофайлы для добавления промо
* dstdir - Каталог куда будут сохранены обработканные файлы
* Может потребоваться подбор параметров сохранения видеофайла. 
