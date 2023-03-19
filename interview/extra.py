 'CONN':mysql_connect('HOST','USER','PASSWORD','NAME'),
        if (!'CONN'){
            die("Connection failed: " . mysql_connect_error()),



if(mysql_query('CONN',data)){
		messages.success(req,"Your data added successfully")
		}
		else
		{
		  messages.warning(req,"Incorrect data") . data . "<br>" . mysql_error('CONN')
		}