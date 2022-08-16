// ignore_for_file: invalid_use_of_protected_member

import 'package:flutter/material.dart';
import 'package:naver_crs/index.dart';
import 'package:get/get.dart';

class HotelCalendarWidget extends StatelessWidget {
  const HotelCalendarWidget({
    Key? key,
    required this.ctx,
    required this.formKey,
  }) : super(key: key);
  final ctx;
  final formKey;
  @override
  Widget build(BuildContext context) {
    filterHotels(context);

    return Form(
      key: formKey,
      child: HotelFiltersWidget(ctx: ctx, formKey: formKey),
    );
  }
}

// ignore: must_be_immutable
class HotelFiltersWidget extends StatelessWidget {
  HotelFiltersWidget({
    Key? key,
    required this.ctx,
    required this.formKey,
  }) : super(key: key);

  final ctx;
  var hotel = "0".obs;
  final formKey;
  @override
  Widget build(BuildContext context) {
    updateHotels();

    return Row(
      children: [
        Column(children: [
          CustomTitleWidget(
              label: "Filter", fontWeight: FontWeight.bold, fontSize: 10),
          SingleChildScrollView(
            child: SizedBox(
              width: Get.width * 0.25,
              // height: Get.height * 0.5,
              child: HotelCalendarFilterWidget(ctx: ctx, formKey: formKey),
            ),
          ),
        ]),
        Column(children: [
          CustomTitleWidget(
              label: "Results", fontWeight: FontWeight.bold, fontSize: 10),
          Obx(() => SizedBox(
                height: Get.height * 0.45,
                // width: Get.width * 0.45,
                child: SingleChildScrollView(
                  child: Column(
                    children: hotels.value,
                  ),
                ),
              )),
        ])
      ],
    );
  }
}

class HotelCalendarFilterWidget extends StatelessWidget {
  const HotelCalendarFilterWidget({
    Key? key,
    required this.ctx,
    required this.formKey,
  }) : super(key: key);

  final ctx;
  final formKey;

  @override
  Widget build(BuildContext context) {
    return SingleChildScrollView(
      scrollDirection: Axis.vertical,
      child: SizedBox(
        width: Get.width * 0.3,
        // height: Get.height * 0.5,
        child: Obx(() {
          return Column(
            children: [
              Row(
                children: [
                  CustomFormDropDownFieldWidget(
                      width: 0.11,
                      height: 0.05,
                      validator: CustomRequiredValidator(
                          errorText: "Hotel Name is required ", ctx: ctx),
                      value: getFormValue(globalctx.memory["destinations"],
                          globalDestinationIndex, "hotelId", "0"),
                      onSaved: (value) {
                        hotelName.value = hotelName.value;
                      },
                      onChanged: (value) {
                        setFormValue(globalctx.memory["destinations"],
                            globalDestinationIndex, "hotelId", value);
                        hotelName.value = getCatalogDescription(
                            getMemoryCatalogChild("hotel", "value", "hotelname",
                                condition: (element) {
                              var rule = true;
                              var filter = hotelResults.value
                                  .map((e) => e["description"])
                                  .toList();
                              rule = rule &&
                                  filter.contains(element["description"]);
                              return rule;
                            }),
                            value);
                        setFormValue(
                            globalctx.memory["destinations"],
                            globalDestinationIndex,
                            "hotelName",
                            hotelName.value);
                        filterHotels(context);
                      },
                      hintText: "Hotel Name     ",
                      data: getMemoryCatalogChild("hotel", "value", "hotelname",
                          condition: (element) {
                        var rule = true;
                        var filter = hotelResults.value
                            .map((e) => e["description"])
                            .toList();
                        rule = rule && filter.contains(element["description"]);
                        return rule;
                      })),
                  CustomFormDropDownFieldWidget(
                      width: 0.11,
                      height: 0.05,
                      validator: CustomRequiredValidator(
                          errorText: "Budget is required ", ctx: ctx),
                      value: budget.value,
                      onSaved: (value) {},
                      onChanged: (value) {
                        budget.value = value!;
                        hotelCategory.value = getCatalogDescription(
                            getMemoryCatalogChild(
                                "hotel", "value", "budget_fk"),
                            value);
                        setFormValue(
                            globalctx.memory["destinations"],
                            globalDestinationIndex,
                            "hotelCategory",
                            hotelCategory.value);
                        filterHotels(context);
                      },
                      hintText: "Budget     ",
                      data:
                          getMemoryCatalogChild("hotel", "value", "budget_fk")),
                ],
              ),
              CustomFormMultiDropDownFieldWidget(
                  value: [],
                  validator: (value) => null,
                  onChanged: (value) {
                    setFormValue(
                        globalctx.memory["destinations"],
                        globalDestinationIndex,
                        "hotelRoomCategoryValue",
                        value);
                    hotelRoomCategory.value = getCatalogDescriptionList(
                        getMemoryCatalogChild("hotel", "value", "roomcategory",
                            condition: (element) {
                          var rule = true;
                          var filter = hotelResults.value
                              .map((e) => e["description"])
                              .toList();
                          rule =
                              rule && filter.contains(element["description"]);
                          return rule;
                        }),
                        value);
                    setFormValue(
                        globalctx.memory["destinations"],
                        globalDestinationIndex,
                        "hotelRoomCategory",
                        hotelRoomCategory.value);
                    filterHotels(context);
                  },
                  onSaved: (value) {
                    setFormValue(
                        globalctx.memory["destinations"],
                        globalDestinationIndex,
                        "hotelRoomCategoryValue",
                        value);
                    hotelRoomCategory.value = getCatalogDescriptionList(
                            getMemoryCatalogChild(
                                "hotel", "value", "roomcategory",
                                condition: (element) {
                              var rule = true;
                              var filter = hotelResults.value
                                  .map((e) => e["description"])
                                  .toList();
                              rule = rule &&
                                  filter.contains(element["description"]);
                              return rule;
                            }),
                            value)
                        .map((e) => e.toString())
                        .toList();
                    setFormValue(
                        globalctx.memory["destinations"],
                        globalDestinationIndex,
                        "hotelRoomCategory",
                        hotelRoomCategory.value);
                    filterHotels(context);
                  },
                  hintText: "Room Category     ",
                  data: getMemoryCatalogChild("hotel", "value", "roomcategory",
                      condition: (element) {
                    var rule = true;
                    var filter = hotelResults.value
                        .map((e) => e["description"])
                        .toList();
                    rule = rule && filter.contains(element["description"]);
                    return rule;
                  })),
              CustomFormMultiDropDownFieldWidget(
                value: hotelFilterMemory.value,
                validator: (value) => null,
                enabled: hotelFilterMemory.value.length < 4,
                onSaved: (value) {
                  hotelFilterMemory.value = getCatalogDescriptionList(
                          findCatalog("more_hotel_filters"), value)
                      .map((e) => e.toString())
                      .toList();
                  setFormValue(
                      globalctx.memory["destinations"],
                      globalDestinationIndex,
                      "hotelFilterMemory",
                      hotelFilterMemory.value);
                  filterHotels(context);
                },
                onChanged: (value) {
                  hotelFilterMemory.value = getCatalogDescriptionList(
                          findCatalog("more_hotel_filters"), value)
                      .map((e) => e.toString())
                      .toList();
                  setFormValue(
                      globalctx.memory["destinations"],
                      globalDestinationIndex,
                      "hotelFilterMemory",
                      hotelFilterMemory.value);
                  filterHotels(context);
                },
                hintText: "More Filters     ",
                label: '',
                data: findCatalog("more_hotel_filters").where((e) {
                  var rule = true;
                  if (hotelResults.value.isNotEmpty) {
                    var filter = hotelResults.value
                        .map((f) => f["value"][e["value"]["key"]] == "Yes")
                        .toSet()
                        .toList()[0];
                    rule = filter;
                  }

                  return rule;
                }).toList(),
              ),
            ],
          );
        }),
      ),
    );
  }
}

class HotelKeyPadWidget extends StatelessWidget {
  const HotelKeyPadWidget({
    Key? key,
    required this.formKey,
  }) : super(key: key);
  final formKey;
  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: EdgeInsets.only(top: Get.height * 0, left: Get.width * 0.4),
      child: Wrap(
        children: [
          TextButton(
            onPressed: () {
              resetHotelField(context, formKey);
            },
            child: Text("Reset",
                style: KTextSytle(
                        context: context,
                        fontSize: 12,
                        fontWeight: FontWeight.bold,
                        color: Colors.black)
                    .getStyle()),
          ),
          TextButton(
            onPressed: () {
              if (formKey.currentState!.validate()) {
                formKey.currentState!.save();
                Get.close(1);
              }
            },
            child: Text("Promote",
                style: KTextSytle(
                        context: context,
                        fontSize: 12,
                        fontWeight: FontWeight.bold,
                        color: Colors.black)
                    .getStyle()),
          ),
        ],
      ),
    );
  }
}

class HotelResultWidget extends StatelessWidget {
  const HotelResultWidget({
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      child: Stack(children: [
        // if (hotelTerraceorPatio.isNotEmpty)
        //   if (hotelMaxCapacity.isNotEmpty)
        //     if (hotelBalcony.isNotEmpty)
        //       if (hotelExtrabed.isNotEmpty)
        //         if (hotelExtrabed.isNotEmpty)
        Column(
          children: [
            Padding(
              padding: EdgeInsets.only(
                top: Get.height * 0.03,
                left: Get.width * 0.0,
              ),
              child: Container(
                width: Get.width * 0.5,
                height: Get.height * 0.03,
                decoration: BoxDecoration(color: Colors.grey),
                child: Row(
                  children: [
                    SizedBox(
                      child: Text(
                        "Hotel Name",
                        textAlign: TextAlign.center,
                        style: TextStyle(
                            fontSize: 12, fontWeight: FontWeight.bold),
                      ),
                    ),
                    SizedBox(
                        child: Text(
                      "Actions",
                      textAlign: TextAlign.center,
                      style:
                          TextStyle(fontSize: 12, fontWeight: FontWeight.bold),
                    )),
                  ],
                ),
              ),
            ),
            SizedBox(
                width: Get.width * 0.8,
                height: Get.height * 0.65,
                child: Stack(
                  children: [
                    SingleChildScrollView(
                      scrollDirection: Axis.vertical,
                      child: Padding(
                        padding: EdgeInsets.only(
                          top: Get.height * 0.0,
                          left: Get.width * 0.03,
                        ),
                        child: Align(
                          alignment: Alignment.topCenter,
                          child: Obx(() => Column(
                                children: [
                                  if (hotelResults.value.isNotEmpty &&
                                      searcherHeader.value.isNotEmpty)
                                    hotelTable.value
                                  else
                                    Text(
                                      "No Hotels Found",
                                      style: KTextSytle(
                                        context: context,
                                        fontSize: 12,
                                        fontWeight: FontWeight.bold,
                                        color:
                                            Color.fromARGB(255, 204, 164, 61),
                                      ).getStyle(),
                                    )
                                ],
                              )),
                        ),
                      ),
                    ),
                  ],
                ))
          ],
        ),
      ]),
    );
  }
}
