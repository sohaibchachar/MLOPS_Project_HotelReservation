from setuptools import setup,find_packages
with open("requirements.txt") as f:
    requirements = f.read().splitlines()
setup(
    name = "Project1_HotelReservationPrediction",
    version= "0.1",
    author= "Sohaib Chachar",
    packages=find_packages(),
    install_requires = requirements
)