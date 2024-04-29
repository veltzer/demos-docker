site="mysql"
env_db_user="root"
env_db_password=$(pass show "passwords/${site}/${env_db_user}")
export env_db_user
export env_db_password
env_db_name="mysql"
export env_db_name
