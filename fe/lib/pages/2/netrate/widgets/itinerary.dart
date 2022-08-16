import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:naver_crs/pages/2/netrate/widgets/customdescription.dart';
import '../../../../index.dart';
import 'cover.dart';
import 'destinations.dart';
import 'header.dart';

class Itinerary extends StatelessWidget {
  Itinerary({Key? key, required this.pkeys}) : super(key: key);

  final _controller = ScrollController();
  final pkeys;
  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: EdgeInsets.only(top: Get.height * 0.05, left: Get.width * 0.05),
      child: Stack(
        children: [
          SizedBox(
            height: Get.height * 1.5,
            width: Get.width * 0.8,
            child: Align(
              alignment: Alignment.center,
              child: Scrollbar(
                child: SingleChildScrollView(
                  controller: _controller,
                  child: Column(children: [
                    RepaintBoundary(key: pkeys["cover"], child: Cover()),
                    RepaintBoundary(
                      key: pkeys["header"],
                      child: Header(),
                    ),
                    Destinations(),
                    Obx(() {
                      return CustomDescriptionWidget(
                          fontWeight: FontWeight.bold,
                          text: "Total Net Rate: \$ $totalNetRate",
                          width: 0.55,
                          fontSize: 18);
                    }),
                  ]),
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}
