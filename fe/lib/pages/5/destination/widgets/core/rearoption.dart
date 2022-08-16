import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:naver_crs/index.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:naver_crs/pages/5/destination/widgets/destinationdetail/widgets/index.dart';

// ignore: must_be_immutable
class DestinationRearOptionWidget extends StatelessWidget {
  const DestinationRearOptionWidget({Key? key, required this.destination})
      : super(key: key);

  final String destination;

  @override
  Widget build(BuildContext context) {
    var value = getDestinationValueByName(destination);
    var title = value["data"][1];
    var description = value["data"][8];
    // title = value["title"];
    return Stack(children: [
      // TitleWidget(title: title),
      DescriptionWidget(title: title, description: description),
    ]);
  }
}

class TitleWidget extends StatelessWidget {
  const TitleWidget({
    Key? key,
    required this.title,
  }) : super(key: key);

  final String title;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: EdgeInsets.only(
        top: Get.height * 0.04,
        left: Get.width * 0.07,
      ),
      child: Row(children: [
        Image.asset("assets/images/1x/Recurso_295mdpi.png",
            width: Get.width * 0.04),
        SizedBox(
          width: title.length * Get.width * 0.01 +
              ((36.6 - title.length) * (Get.width) * 0.018 / 10),
        ),
        Image.asset("assets/images/1x/Recurso_294mdpi.png",
            width: Get.width * 0.04),
      ]),
    );
  }
}

class DescriptionWidget extends StatelessWidget {
  const DescriptionWidget({
    Key? key,
    required this.title,
    required this.description,
  }) : super(key: key);

  final String title;
  final String description;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: EdgeInsets.only(
        top: Get.height * 0.05,
        left: Get.width * 0.05,
      ),
      child: Align(
          alignment: Alignment.center,
          child: SizedBox(
            width: Get.width * 0.3,
            child: Wrap(
              children: [
                Text(
                  title,
                  style: GoogleFonts.poppins(
                      textStyle: TextStyle(
                    color: const Color.fromARGB(255, 204, 164, 61),
                    fontSize: 12,
                    fontWeight: FontWeight.bold,
                  )),
                ),
                TextButton(
                  onPressed: () {
                    showCustomDialog(
                      context,
                      DestinationDetailLeftWidget(
                          destination: "quito", index: 0),
                      "Close",
                      buttonColor: Colors.white,
                    );
                  },
                  child: Text(
                    description,
                    style: GoogleFonts.poppins(
                        textStyle: TextStyle(
                      color: const Color.fromARGB(255, 128, 128, 128),
                      fontSize: 12,
                      fontWeight: FontWeight.bold,
                    )),
                  ),
                ),
              ],
            ),
          )),
    );
  }
}
