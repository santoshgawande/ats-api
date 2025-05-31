from candidates.models import Candidate

candidates = [
    Candidate(
        name="Ajay Kumar Yadav",
        age=29,
        gender="Male",
        email="ajay.yadav@example.com",
        phone_number="9000010001",
    ),
    Candidate(
        name="Ajay Kumar",
        age=31,
        gender="Male",
        email="ajay.kumar@example.org",
        phone_number="9000010002",
    ),
    Candidate(
        name="Ajay Yadav",
        age=27,
        gender="Male",
        email="ajay.yadav2@example.net",
        phone_number="9000010003",
    ),
    Candidate(
        name="Kumar Yadav",
        age=33,
        gender="Male",
        email="kumar.yadav@example.com",
        phone_number="9000010004",
    ),
    Candidate(
        name="Ramesh Yadav",
        age=40,
        gender="Male",
        email="ramesh.yadav@example.com",
        phone_number="9000010005",
    ),
    Candidate(
        name="Ajay Singh",
        age=25,
        gender="Male",
        email="ajay.singh@example.com",
        phone_number="9000010006",
    ),
]

Candidate.objects.bulk_create(candidates)
print("Sample candidates inserted successfully.")
