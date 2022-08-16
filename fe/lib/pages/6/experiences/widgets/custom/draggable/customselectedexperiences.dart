import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:naver_crs/index.dart';
import 'package:naver_crs/pages/6/experiences/widgets/custom/draggable/experiencedragtarget.dart';

class CustomSelectedExperiencesWidget extends StatelessWidget {
  const CustomSelectedExperiencesWidget({
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return SingleChildScrollView(
      child: SizedBox(
          width: Get.width * 0.3,
          height: Get.height * 0.5,
          child: Wrap(
            children: [
              CustomTitleWidget(
                  fontWeight: FontWeight.bold,
                  label: "Selected Experiences",
                  color: Colors.white),
              Scrollbar(
                child: SingleChildScrollView(
                  child: ExperienceDragTargetWidget(
                    onAccept: (String experience) {
                      if (experience == "Leisure Time" &&
                          leftHours[currentDay.value].value <= 0) {
                        return;
                      } else {
                        promoteExperience(experience, "promoted");
                      }
                    },
                  ),
                ),
              ),
            ],
          )),
    );
  }
}
