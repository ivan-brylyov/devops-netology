# Домашнее задание к занятию "5.2. Системы управления виртуализацией"

## Задача 1 

Выберете подходящую систему управления виртуализацией для предложенного сценария. Детально опишите ваш выбор.

Сценарии:

- 100 виртуальных машин на базе Linux и Windows, общие задачи, нет особых требований 	
	 - KVM, Xen, т.к. XenPV позволяет развертывать гостевые ВМ с помощью шаблонов. При этом в KVM лучше поддержка Windows, поэтому нужно исходить из приоритета производительности/надежности в конкретном случае.

- Преимущественно Windows based инфраструктура, требуется реализация программных балансировщиков нагрузки, репликации данных и автоматизированного механизма создания резервных копий 
	 - Hyper-V, т.к. имеет все перечисленные возможности. 

- Требуется наиболее производительное бесплатное opensource решение для виртуализации небольшой (20 серверов) инфраструктуры Linux и Windows виртуальных машин
	 - KVM, как наиболее производительное решение.

- Необходимо бесплатное, максимально совместимое и производительное решение для виртуализации Windows инфраструктуры 
	 - Hyper-V - встроен в Windows Server, кроме того существует Microsoft Hyper-V Server, бесплатная ОС с единственной ролью - сервером виртуализации. KVM.

- Необходимо рабочее окружение для тестирование программного продукта на нескольких дистрибутивах Linux
	 - Docker или другие контейнеры, Xen, KVM


## Задача 2

Опишите сценарий миграции с VMware vSphere на Hyper-V для Linux и Windows виртуальных машин. Детально опишите необходимые шаги для использования всех преимуществ Hyper-V для Windows.

	Если я правильно понял понятие миграции и вообще вопрос - есть 2 способа, онлайн и офлайн миграция. 
	Онлайн - миграция "наживую", т.е. с минимальным временем недоступности ВМ. Происходит копирование работающей машины, и лишь в конце происходит выключение машины, клпирование оставшихся данных и включение.
	Офлайн-миграция происходит при выключенной ВМ. Важным моментом является конвертация VMDK-диска в VHD, суть - модификация файла виртуального диска. Все параметры виртальной машины при этом могут быть скопированы как есть, т.к. машина выключена. В отличие от онлайн-миграции требует некоторого времени простоя ВМ.


## Задача 3 

Опишите возможные проблемы и недостатки гетерогенной среды виртуализации (использования нескольких систем управления виртуализацией одновременно) и что необходимо сделать для минимизации этих рисков и проблем. Если бы у вас был бы выбор, то создавали ли вы бы гетерогенную среду или нет? Мотивируйте ваш ответ примерами. 

	-: Для администрирования нескольких систем требуется наличие навыков у администратора по каждой из них, либо нескольких администраторов, т.е. денег.
	Сами по себе системы могут быть небесплатными, что так же влечет затраты.
	Возможны проблемы при миграции ВМ.

	+: В теории, при эксплуатации зоопарка ОС из разных Linux и Windows совершенно необходимым будет наличие нескольких систем управления из-за проблем совместимости, но это, скорее, частный случай.