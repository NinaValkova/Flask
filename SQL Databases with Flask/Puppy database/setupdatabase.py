from basic import db, Puppy, app  # make sure you import app from your main file

with app.app_context():
    db.create_all()

    sam = Puppy('Sammy', 3, "dog breed")
    frank = Puppy('Frankie', 4, "dog breed")

    db.session.add_all([sam, frank])
    db.session.commit()

    print(f"Database created and puppies added! {sam.id}, {frank.id}")
