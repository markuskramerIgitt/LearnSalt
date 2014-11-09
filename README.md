File /srv/salt/top.sls contains


base:
  '*':
    - LearnSalt/learn-run-as
    - LearnSalt/learn-unless


