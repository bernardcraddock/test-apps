late String _title;  // Declare a non-nullable variable


void _showTitle () async {
  // Simulate fetching data from an API
  await Future.delayed (Duration (seconds: 2));   

  // Set the value of _title
  _title = 'GeekdForGeeks';   

  // print the title to the console 
 print('Late is Initialized by text : ${_title}');
}

void main() {
	_showTitle();
}
