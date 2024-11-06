import subprocess


# def run_alembic_init():
#     try:
#         # Execute the command 'alembic init alembic' programmatically
#         subprocess.run(["alembic", "init", "alembic"], check=True)
#         print("Alembic initialization completed.")
#     except subprocess.CalledProcessError as e:
#         print(f"An error occurred while initializing Alembic: {e}")
# run_alembic_init()


# def create_alembic_revision():
#     try:
#         # Execute the command 'alembic revision -m "Create phone number for user column"'
#         subprocess.run(["alembic", "revision", "-m", "Create phone number for user column"], check=True)
#         print("Alembic revision created successfully.")
#     except subprocess.CalledProcessError as e:
#         print(f"An error occurred while creating the revision: {e}")
#
#
# create_alembic_revision()

# Call the function to run the command


def run_alembic_upgrade(upgrade_id):
    try:
        # Execute the command 'alembic revision -m "Create phone number for user column"'
        subprocess.run(["alembic", "upgrade", upgrade_id], check=True)
        print("Alembic upgrade done successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while creating the revision: {e}")


run_alembic_upgrade('c926fac692da')

# def run_alembic_downgrade():
#     try:
#         # Execute the command 'alembic revision -m "Create phone number for user column"'
#         subprocess.run(["alembic", "downgrade", "-1"], check=True)
#         print("Alembic upgrade done successfully.")
#     except subprocess.CalledProcessError as e:
#         print(f"An error occurred while creating the revision: {e}")
#
#
# run_alembic_downgrade()
