<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>EC Dragon Test</title>
</head>
<body>
<pre>
<?php

$test = array(
	array('abc', 'abc'), //0
	array('kitten', 'sitting'), //3
	array('������', '�߂���'), //5
	array('�Ɩ�', '��'), //
	array('������', '������'), //
	array('�������̂���', '����'), //
	array('�Ύ�', '�ԉ�'), //
	array('�Ύ�', '����'), //
	array('smei', 'mei'), //
	array('12345', '234'),
);
foreach ($test as $row) {
	echo $row[0].','.$row[1];
	echo ' | ';
	echo levenshtein($row[0], $row[1]);
	echo ' = ';
	var_dump(LevenshteinDistance($row[0], $row[1]));
	echo '<br/>';
}

?>

</pre>
</body>
</html>