param(
  [string]$Host = "127.0.0.1",
  [string]$User = "postgres",
  [string]$Db   = "login_db"
)
psql -h $Host -U $User -c "CREATE DATABASE $Db;"
psql -h $Host -U $User -d $Db -f "..\db\db.sql"
psql -h $Host -U $User -d $Db -f "..\db\seed.sql"
