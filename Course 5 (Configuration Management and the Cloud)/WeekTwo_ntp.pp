class ntp {
    
    package { 'ntp':
        ensure => latest,
    }
    
    file { '/etc/ntp.conf':
        source => 'puppet:///modules/ntp/ntp.conf',
        replace => true,
       require => Package['ntp'],
        notify => Service['ntp'],
    }
    
    service { 'ntp':
        enable => true,
        ensure => running,
        # service requires the configuration file
        require => File['/etc/ntp.conf'],
    }
}

include ntp
