from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        movie: str,
        customers: list,
        hall_number: int,
        cleaner: str
) -> None:
    # Criar instâncias de Customer e vender produtos no bar
    customer_instances = []
    for person in customers:
        customer_obj = Customer(name=person["name"], food=person["food"])
        customer_instances.append(customer_obj)
        CinemaBar.sell_product(product=customer_obj.food, customer=customer_obj)

    # Criar instâncias do Hall e do Cleaner
    hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    # Iniciar a sessão (que inclui assistir ao filme e a limpeza)
    hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaning_staff
    )
