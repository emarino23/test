import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'cover.dart';
import 'destinations.dart';
import 'header.dart';

class Itinerary extends StatelessWidget {
  Itinerary({Key? key, required this.pkeys}) : super(key: key);

  final _controller = ScrollController();
  final pkeys;
  @override
  Widget build(BuildContext context) {
    return Stack(
      children: [
        Padding(
          padding:
              EdgeInsets.only(top: Get.height * 0.4, left: Get.width * 0.1),
          child: SizedBox(
            height: Get.height * 1.5,
            width: Get.width * 0.8,
            child: Center(
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
                  ]),
                ),
              ),
            ),
          ),
        ),
      ],
    );
  }
}
