from basic import db, Puppy, app

with app.app_context():
    my_puppy = Puppy('Rufas', 5, "dog breed")
    db.session.add(my_puppy)
    db.session.commit()

    all_puppies = Puppy.query.all()
    print(all_puppies)

    puppy_one = Puppy.query.get(1)
    print(puppy_one)

    puppy_frankie = Puppy.query.filter_by(name='Frankie')
    print(puppy_frankie.all())

    first_puppy = Puppy.query.get(1)
    if first_puppy:
        first_puppy.age = 10
        db.session.commit()

    second_pup = Puppy.query.get(2)
    if second_pup:
        db.session.delete(second_pup)
        db.session.commit()

    all_puppies = Puppy.query.all()
    print(all_puppies)
