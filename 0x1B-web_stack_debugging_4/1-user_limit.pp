# 1. User limit
exec { 'update soft limit':
  provider => shell,
  command  => 'sed -i s/holberton/"# holberton"/ /etc/security/limits.conf'
}