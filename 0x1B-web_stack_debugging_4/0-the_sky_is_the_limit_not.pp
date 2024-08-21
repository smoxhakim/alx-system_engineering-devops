# 0. Sky is the limit, let's bring that limit higher
exec { 'update ulimit':
  provider => shell,
  command  => 'sed -i s/15/1000000/ /etc/default/nginx'
}
exec { 'restart nginx':
  provider => shell,
  command  => 'service nginx restart'
}