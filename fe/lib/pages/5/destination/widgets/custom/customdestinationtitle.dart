import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:google_fonts/google_fonts.dart';
import '../../../../../index.dart';

class CustomDestinationTitleWidget extends StatelessWidget {
  const CustomDestinationTitleWidget({
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Positioned(
      top: Get.height * 0.1,
      left: Get.width * 0.1,
      child: Obx(() {
        var t = arrivalDate.value;
        return Row(
          children: [
            Text("Remaining Days: ",
                style: GoogleFonts.poppins(
                    textStyle: TextStyle(
                  color: (dayleft.value) < 1
                      ? Colors.yellow
                      : Color.fromARGB(255, 0, 255, 0),
                  fontSize: 15,
                  fontWeight: FontWeight.bold,
                ))),
            // if (accumulated.value >= totalDays.value)
            Text(
                accumulated.value >= totalDays.value ? "0" : dayleft.toString(),
                style: GoogleFonts.poppins(
                    textStyle: TextStyle(
                  color: (dayleft.value) < 1
                      ? Colors.yellow
                      : Color.fromARGB(255, 0, 255, 0),
                  fontSize: 15,
                  fontWeight: FontWeight.bold,
                ))),

            Text("    Selected Days: $accumulated",
                style: GoogleFonts.poppins(
                    textStyle: TextStyle(
                  color: (accumulated.value) == 0
                      ? Color.fromARGB(255, 0, 255, 0)
                      : Colors.yellow,
                  fontSize: 15,
                  fontWeight: FontWeight.bold,
                ))),
          ],
        );
      }),
    );
  }
}
