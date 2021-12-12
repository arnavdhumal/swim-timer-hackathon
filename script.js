function select_sport() {
    var sportvalue = document.getElementById("sport").value;
    if (sportvalue == "Swimming") {
        document.getElementById("swim_form").style = 'block';
        function start() {
            console.log("start")
        }
        function lap() {
            console.log("lap")
        }
        function end() {
            console.log("end")
        }
    }
}
