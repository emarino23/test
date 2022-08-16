import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:google_fonts/google_fonts.dart';

import '../../../../../index.dart';

class DestinationIndexControlWidget extends StatelessWidget {
  const DestinationIndexControlWidget({
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Obx(() => Text("Destination Index: $globalDestinationIndex",
        style: GoogleFonts.poppins(
            textStyle: TextStyle(
          color: (dayleft.value) < 1
              ? Colors.yellow
              : Color.fromARGB(255, 0, 255, 0),
          fontSize: 15,
          fontWeight: FontWeight.bold,
        ))));
  }
}
