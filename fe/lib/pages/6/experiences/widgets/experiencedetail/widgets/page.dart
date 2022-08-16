// ignore_for_file: invalid_use_of_protected_member

import 'package:flutter/material.dart';
import '../index.dart';
import 'index.dart';
import 'package:naver_crs/index.dart';
import 'package:get/get.dart';

class ExperienceDetailWidget extends GetView<ExperienceDetailController> {
  const ExperienceDetailWidget({Key? key, this.experience}) : super(key: key);
  final experience;
  @override
  Widget build(BuildContext context) {
    var expCode = Rx(getExperienceDataByName(experience).code);
    var expValue = Rx(getExperienceDataByName(experience).value);
    return Stack(
      children: [
        SingleChildScrollView(
          child: Padding(
            padding:
                EdgeInsets.only(left: Get.width * 0.0, top: Get.height * 0.0),
            child: Column(
              children: [
                TitleWidget(experience: experience),
                TextButton(
                    onPressed: () {
                      showCustomDialog(
                          context,
                          YoutubeWidget(
                            videoId: expValue.value["video"],
                          ),
                          "Close",
                          backgroundColor: Color.fromARGB(100, 0, 0, 0),
                          buttonColor: Colors.white);
                    },
                    child: Text("    click here to watch video",
                        style: KTextSytle(
                                context: context,
                                fontSize: 12,
                                fontWeight: FontWeight.bold,
                                color: Colors.grey)
                            .getStyle())),
                Obx(() => LeftGalleryWidget(
                    catalog: "experiences",
                    code: expCode.value.toString(),
                    value: "images")),
                DescriptionWidget(experience: experience),
                if (getExperienceState(experience) != "suggested")
                  KeypadWidget(experience: experience),
              ],
            ),
          ),
        ),
      ],
    );
  }
}
