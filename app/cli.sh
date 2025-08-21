#!/bin/sh
. ./environments.sh

cmd_wqdms_backend_mig(){
    python3 manage.py makemigrations
    python3 manage.py migrate
}

cmd_wqdms_backend_dump(){
    python3 manage.py dumpdata auth.user > ./interactive/admin.json
    python3 manage.py dumpdata interface > ./interactive/interface.json
}

cmd_wqdms_backend_start(){
    cmd_wqdms_backend_mig
    python3 manage.py loaddata ./interactive/admin.json
    python3 manage.py loaddata ./interactive/interface.json
    python3 manage.py runserver 0.0.0.0:8000
}
cmd_wqdms_jupyter_start(){
    python3 manage.py shell_plus --lab
}

cmd_wqdms_backend_purge(){
    rm ./db.sqlite3
    MIGS='interface sensorthings waterquality'
    for i in $MIGS;do
        f="./$i/migrations"
        p="./$i/__pycache__"
        rm -drf $f
        rm -drf $p
        echo "removed $f"
        mkdir -p $f
        touch $f/__init__.py
    done
}

cmd_python_remove_pycache(){
    for i in $(find ./ -name __pycache__ -type d);do 
        rm -drf $i 
    done
}

cmd_wqdms_shiny_server(){
    shiny run --host 0.0.0.0 --port 8001 --reload /app/interactive/shiny/server.py
}

cmd_wqdms_shell_plus_lab(){
    python3 manage.py shell_plus --lab
}