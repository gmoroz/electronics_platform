from django.db import models


class Address(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.PositiveIntegerField()

    def __str__(self):
        return self.full_address

    @property
    def full_address(self):
        return f"{self.house_number}, {self.street} {self.country}, {self.city}"

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"


class Contact(models.Model):
    email = models.EmailField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.address}"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"


class Product(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    release_date = models.DateField()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Employee(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"


class NetworkObj(models.Model):
    name = models.CharField(max_length=100, unique=True)
    contacts = models.ManyToManyField(Contact)
    products = models.ManyToManyField(Product)
    employees = models.ManyToManyField(Employee)
    debt_value = models.DecimalField(decimal_places=2, default=0, max_digits=11)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    @property
    def provider_name(self):
        return self.provider.__class__.__name__.lower()

    @property
    def debt(self):
        return "{} RUR".format(self.debt_value)

    class Meta:
        abstract = True


class Plant(models.Model):
    name = models.CharField(max_length=100, unique=True)
    contacts = models.ManyToManyField(Contact)
    products = models.ManyToManyField(Product)
    employees = models.ManyToManyField(Employee)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Завод"
        verbose_name_plural = "Заводы"


class RetailChain(NetworkObj):
    provider = models.ForeignKey(Plant, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Розничная сеть"
        verbose_name_plural = "Розничные сети"


class Businessman(NetworkObj):
    provider = models.ForeignKey(RetailChain, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Индивидуальный предприниматель"
        verbose_name_plural = "Индивидуальные предприниматели"


class Network(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    retail_chain = models.ForeignKey(RetailChain, on_delete=models.CASCADE)
    businessman = models.ForeignKey(Businessman, on_delete=models.CASCADE)

    @property
    def name(self):
        return f"Сеть № {self.id}"

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сеть поставщиков"
        verbose_name_plural = "Сети поставщиков"
