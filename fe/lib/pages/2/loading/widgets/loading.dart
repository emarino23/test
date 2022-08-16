import 'package:flutter/material.dart';
import 'package:naver_crs/index.dart';
import 'package:get/get.dart';

/// Loading
// ignore: must_be_immutable
class LoadingWidget extends GetView<LoadingController> {
  LoadingWidget({
    Key? key,
    required this.ctrl,
  }) : super(key: key);
  LoadingController ctrl;
  RxBool newtour = true.obs;
  @override
  Widget build(BuildContext context) {
    return Align(
      alignment: Alignment.bottomCenter,
      child: BodyLayoutWidget(
          background: "assets/images/1x/loading.png",
          child: Stack(
            children: [
              Padding(
                  padding: EdgeInsets.only(
                      left: Get.width * 0.45, top: Get.height * 0.6),
                  child: Column(
                    children: [
                      RoundedFormButton(
                        textColor: Color.fromARGB(255, 204, 164, 61),
                        color: Colors.white,
                        label: "New Tour",
                        fontSize: 16,
                        height: Get.height * 0.06,
                        width: Get.width * 0.02,
                        onPressed: () async {
                          var res = await getCatalogs(["ALL"]);
                          if (res) {
                            await newTour();
                          }
                          setContext("readonly", false);
                        },
                      ),
                      SizedBox(
                        height: Get.height * 0.02,
                      ),
                      RoundedFormButton(
                        textColor: Color.fromARGB(255, 204, 164, 61),
                        color: Colors.white,
                        label: "Find Tour",
                        fontSize: 16,
                        height: Get.height * 0.06,
                        width: Get.width * 0.02,
                        onPressed: () async {
                          await getCatalogs(
                              ["experiences", "hotel", "cruises", "cabine"]);
                          await getTour(context, tourId: 0, cb: (data) {
                            if (data.length > 0) {
                              globalctx.memory["tours"] = data;
                              if (0 == 0) {
                                Get.toNamed("/Searcher");
                              } else {
                                Get.toNamed("/Tour");
                              }
                            }
                          });
                        },
                      ),
                    ],
                  )),
            ],
          )),
    );
  }
}
