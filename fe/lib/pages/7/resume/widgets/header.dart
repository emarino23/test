import 'package:counter/counter.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:naver_crs/index.dart';
import 'package:naver_crs/pages/2/netrate/widgets/custompadingtitle.dart';
import 'customformtitle.dart';

class Header extends StatelessWidget {
  const Header({
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    try {
      return Column(
        children: [
          const CustomFormTitleWidget(level: 1, label: "Customer Information"),
          Row(
            children: [
              CustomDetailWidget(
                  label: "Names: ",
                  value:
                      getFormValue(globalctx.memory, "customer", "names", '')),
              CustomDetailWidget(
                  label: "Last Names: ",
                  value: getFormValue(
                      globalctx.memory, "customer", "last_names", '')),
            ],
          ),
          Row(
            children: [
              CustomDetailWidget(
                  label: "Lead Passenger: ",
                  value: getFormValue(
                      globalctx.memory, "tour", "lead_passenger", '')),
              CustomDetailWidget(
                  label: "dni: ",
                  value: getFormValue(
                      globalctx.memory, "customer", "client_dni", '')),
              CustomDetailWidget(
                  label: "email: ",
                  value:
                      getFormValue(globalctx.memory, "customer", "email", '')),
            ],
          ),
          Row(
            children: [
              CustomDetailWidget(
                  label: "Address Line: ",
                  value: getFormValue(
                      globalctx.memory, "customer", "address", '')),
              CustomDetailWidget(
                  label: "City: ",
                  value: getCity(
                          getFormValue(
                              globalctx.memory, "customer", "state_id", 1),
                          getFormValue(globalctx.memory, "customer", "city_id",
                              1))["description"] ??
                      "".toString().capitalize),
              CustomDetailWidget(
                  label: "State: ",
                  value: getState(getFormValue(globalctx.memory, "customer",
                          "state_id", 1))["description"] ??
                      "".toString().capitalize),
              CustomDetailWidget(
                  label: "Country: ",
                  value: getCountry()["description"].toString().capitalize),
            ],
          ),
          const CustomFormTitleWidget(level: 1, label: "Tour Information"),
          Row(
            children: [
              CustomDetailWidget(
                  label: "Tour Code: ",
                  value: getFormValue(globalctx.memory, "tour", "code", '0')),
              CustomDetailWidget(
                  label: "Passengers: ",
                  value: getFormValue(
                      globalctx.memory, "tour", "passengers", '0')),
              CustomDetailWidget(
                  label: "Budget: ",
                  value: findCatalog("budget")
                      .toList()
                      .firstWhere((element) =>
                          element["code"].toString() ==
                          getFormValue(globalctx.memory, "tour",
                                  "accomodation_type", '0')
                              .toString())["description"]
                      .toString()
                      .capitalize),
              CustomDetailWidget(
                  label: "Country: ",
                  value:
                      getFormValue(globalctx.memory, "customer", "country", 1)),
            ],
          ),
          const CustomFormTitleWidget(level: 1, label: "Logistic Information"),
          Row(
            children: [
              CustomDetailWidget(
                  label: "Arrival Port: ",
                  value: findCatalog("destinations")
                      .toList()
                      .firstWhere((element) =>
                          element["code"].toString() ==
                          arrivalPort.value.toString())["description"]
                      .toString()
                      .capitalize),
              CustomDetailWidget(
                  label: "Departure Port: ",
                  value: findCatalog("destinations")
                      .toList()
                      .firstWhere((element) =>
                          element["code"].toString() ==
                          departurePort.value.toString())["description"]
                      .toString()
                      .capitalize),
              CustomDetailWidget(
                  label: "Tour option: ",
                  value: findCatalog("tour_option")
                      .toList()
                      .firstWhere((element) =>
                          element["code"].toString() ==
                          tourOption.value.toString())["description"]
                      .toString()
                      .capitalize),
            ],
          ),
          Row(
            children: [
              CustomDetailWidget(
                  label: "Arrival Date: ",
                  value: currentDayFormat.format(arrivalDate.value)),
              CustomDetailWidget(
                  label: "Departure Date: ",
                  value: currentDayFormat.format(departureDate.value)),
            ],
          ),
          CustomFormTitleWidget(
              level: 2,
              label:
                  "Itinerary #(Between: ${currentDayFormat.format(arrivalDate.value)} and ${currentDayFormat.format(departureDate.value)})"),
          Row(
            children: [
              CustomPadingTitleWidget(
                  customlabel: "    Guides:        ",
                  fontWeight: FontWeight.bold),
              Counter(
                configuration: CounterConfig(fontSize: 14),
                initial: getGuides(),
                min: 0,
                max: 50,
                step: 1,
                onValueChanged: (value) {
                  if (value > 0) {
                    setFormValue(
                        globalctx.memory, "tour", "translator_guide", true);
                  } else {
                    setFormValue(
                        globalctx.memory, "tour", "translator_guide", false);
                  }
                  setFormValue(globalctx.memory, "tour", "guides", value);
                },
              ),
            ],
          ),
        ],
      );
    } catch (e) {
      return Text("");
    }
  }
}

class OptionField extends StatelessWidget {
  const OptionField({
    Key? key,
    this.label,
    this.data,
    required this.onChange,
  }) : super(key: key);
  final label;
  final data;
  final Function onChange;
  @override
  Widget build(BuildContext context) {
    var groupValue = 0.obs;
    changeField(value) {
      groupValue.value = value;
      onChange(value);
    }

    var dataField = <Widget>[];
    for (var i = 0; i < data.length; i++) {
      dataField.add(
        Obx(() => Radio(
            value: i, groupValue: groupValue.value, onChanged: changeField)),
      );
    }
    return Row(
      children: [
        CustomPadingTitleWidget(
            customlabel: label, fontWeight: FontWeight.bold),
        ...dataField
      ],
    );
  }
}

class CustomDetailWidget extends StatelessWidget {
  const CustomDetailWidget({
    Key? key,
    this.label,
    this.value,
  }) : super(key: key);
  final label;
  final value;
  @override
  Widget build(BuildContext context) {
    try {
      return Padding(
        padding: EdgeInsets.only(
          left: Get.width * 0.05,
          top: Get.height * 0.001,
        ),
        child: Row(
          children: [
            CustomFormLabelWidget(
              label: label,
              fontWeight: FontWeight.bold,
            ),
            CustomFormLabelWidget(label: value.toString()),
          ],
        ),
      );
    } catch (e) {
      return Text("");
    }
  }
}
