from extensions import db
from models import Hero, Power, HeroPower
from app import app

# Seed data function
def seed_data():
    with app.app_context():
        # Drop all tables and recreate them
        db.drop_all()
        db.create_all()

        # Create sample heroes
        hero_1 = Hero(name='Bruce Wayne', super_name='Batman')
        hero_2 = Hero(name='Clark Kent', super_name='Superman')
        hero_3 = Hero(name='Diana Prince', super_name='Wonder Woman')

        # Add heroes to the session
        db.session.add_all([hero_1, hero_2, hero_3])

        # Create sample powers
        power_1 = Power(name='Super Strength', description='Can lift heavy objects and overpower enemies.')
        power_2 = Power(name='Flight', description='Can fly through the air at incredible speeds.')
        power_3 = Power(name='Invisibility', description='Can become invisible to the naked eye.')

        # Add powers to the session
        db.session.add_all([power_1, power_2, power_3])

        # Commit heroes and powers to the database
        db.session.commit()

        # Create sample hero powers (assigning powers to heroes)
        hero_power_1 = HeroPower(strength='strong', hero_id=hero_2.id, power_id=power_1.id)  # Superman has Super Strength
        hero_power_2 = HeroPower(strength='moderate', hero_id=hero_1.id, power_id=power_2.id)  # Batman has Flight (with gadgets)
        hero_power_3 = HeroPower(strength='strong', hero_id=hero_3.id, power_id=power_3.id)  # Wonder Woman has Invisibility

        # Add hero powers to the session
        db.session.add_all([hero_power_1, hero_power_2, hero_power_3])

        # Commit hero powers to the database
        db.session.commit()

        print("Database seeded!")

if __name__ == '__main__':
    seed_data()
