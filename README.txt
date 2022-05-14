To Run Task1:
1. First need to run default controller in terminal from pox folder
Command : ./pox.py forwarding.l2_learning
2. Then will run part1.py from assignment3starter/topos folder 
Command: sudo python3 part1.py
2.1 Other command that can be run in mininet : pingall; iperf h1 h2; iperf h2 h3; net

3. To see rules of controller in terminal from any folder.
Command: sudo ovs-ofctl --protocols OpenFlow13 dump-flows s1 


To Run Task2:
1. First need to run part2 controller in terminal from pox folder
Command : ./pox.py part2controller
2. Then will run part2.py from assignment3starter/topos folder 
Command: sudo python3 part2.py
2.1 Other command that can be run in mininet : pingall; iperf h1 h2; iperf h1 h4; net

3. To see rules of controller in terminal from any folder.
Command: sudo ovs-ofctl --protocols OpenFlow13 dump-flows s1 


To Run Task3:
1. First need to run part3 controller in terminal from pox folder
Command : ./pox.py part3controller
2. Then will run part3.py from assignment3starter/topos folder 
Command: sudo python3 part3.py
2.1 Other command that can be run in mininet : pingall; iperf h10 serv1; iperf hnotrust1, h10; iperf hnotrust1, serv1; net

3. To see rules of controller in terminal from any folder.
Command: sudo ovs-ofctl --protocols OpenFlow13 dump-flows s1; sudo ovs-ofctl --protocols OpenFlow13 dump-flows s2; sudo ovs-ofctl --protocols OpenFlow13 dump-flows s3; sudo ovs-ofctl --protocols OpenFlow13 dump-flows cores21; sudo ovs-ofctl --protocols OpenFlow13 dump-flows dcs31 


