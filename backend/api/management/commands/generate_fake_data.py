import inquirer
from faker import Faker
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model 


User = get_user_model()

fake = Faker()

class Command(BaseCommand):
    help = 'CLI feita para popular o banco de dados de forma interativa'

    def handle(self, *args, **options):
        self.main_menu()

    def main_menu(self):
        while True:
            questions = [
                inquirer.List(
                    'action',
                    message="Escolha uma das opções abaixo",
                    choices=[
                        ('Popular o banco de dados fake', 'create_users'),
                        ('Limpar dados do banco de dados', 'clean_data'),
                        ('Sair', 'exit'),
                    ],
                ),
            ]
            
            answers = inquirer.prompt(questions)
            
            if answers['action'] == 'create_users':
                self.create_fake_users()
            elif answers['action'] == 'clean_data':
                self.clean_data()
            elif answers['action'] == 'exit':
                self.stdout.write(self.style.SUCCESS('Até logo!'))
                break

    def create_fake_users(self):
        questions = [
            inquirer.Text('count', message="Quantos usuários criar?", default="5"),
            inquirer.Confirm('confirm', message="Confirmar criação?"),
        ]
        
        answers = inquirer.prompt(questions)
        
        if answers['confirm']:
            print("Happyyyy")