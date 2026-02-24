late String _title;  // Declare a non-nullable variable
                                                                               // Flutter 
void _showTitle (BuildContext context) async {                                 // BuildContext 
  // Simulate fetching data from an API
  await Future.delayed (Duration (seconds: 2));   

  // Set the value of _title
  _title = 'GeekdForGeeks';   

  // Show the title in a dialog
  showDialog (                                                                 // showDialog 
    context: context,
    builder: (context) => AlertDialog (                                        // AlertDialog 
      title: Text (_title),                                                    // Text 
      content: Text ('Late is Initialized by text : ${_title}'),
      actions: [
        TextButton (                                                           // TextButton 
          onPressed: () => Navigator.pop (context),                            // Navigator
          child: Text ('OK'),
        ),
      ],
    ),
  );
}
