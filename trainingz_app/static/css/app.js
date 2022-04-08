document.addEventListener("DOMContentLoaded", function () {
                                console.log("DOM fully loaded and parsed!");
                            });
                            document.addEventListener("DOMContentLoaded", function () {
                                document.querySelectorAll('#completed').forEach(function(item) {
                                    if (item.innerText === "Completed") {
                                        document.getElementById('text_1').style.color = "green";
                                    }});
                                });





                                function f_color1() {
                                    if (document.getElementById('completed').innerText === "Completed") {
                                        document.getElementById('text_1').style.color = "green";
                                    }
                                }
                                f_color1();