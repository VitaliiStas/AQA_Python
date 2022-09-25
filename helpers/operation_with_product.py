import os

install_location = "C:\\Users\\vitalii.stasiv\\Desktop\\AQA_mentorship\\ap_for_the_python\\juice-shop-master\\juice-shop-master"


def run_command(command):
    return os.system(command)


def start_server():
    os.chdir(install_location)
    run_command("npm run start")




