# using puppet to kill a process named killmenow
exec { 'killmenow_process':
  command => 'pkill -f killmenow',
  path    => '/usr/bin:/usr/sbin:/bin:/sbin',
  onlyif  => 'pgrep -f killmenow',
}
