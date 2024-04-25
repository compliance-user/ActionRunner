import argparse
import pandas
import requests


parser = argparse.ArgumentParser()

parser.add_argument("--azure_application_secret", help="Azure Application Secret", required=True)
parser.add_argument("--azure_application_id", help="Azure Application ID", required=True)
parser.add_argument("--azure_subscription_id", help="Azure Subscription ID", required=True)

args = parser.parse_args()


class RecommendationTypeGuid:
    IDS = [
        "00b1ef72-4d0f-4452-a6a8-1df5397172d6",
        "00c14add-2aef-4bb4-a3bd-5759096d4417",
        "010692cc-0668-43fa-b7dc-6766efb22e59",
        "0169a2e1-c7bf-4c37-90b8-0714811c82d3",
        "01b1ed4c-b733-4fee-b145-f23236e70cf3",
        "01dea77b-3ca4-4583-9b09-88f5a8fd5857",
        "02e8ca50-0e7e-cc34-0b91-215af2904248",
        "0396b18c-41aa-489c-affd-4ee5d1714a59",
        "03afeb6f-7634-adb3-0a01-803b0b9cb611",
        "04e5099a-9064-4e52-8f3b-322c54dc4cf9",
        "061dcd4a-2090-4ec0-b4e0-ec9eaae5cf80",
        "0677209d-e675-2c6f-e91a-54cef2878663",
        "06ac6ef4-1e66-1334-5418-6e79ab444ce0",
        "06ad499a-0952-48d3-b061-ec81c9cabb8b",
        "07f9a07d-9030-465c-89dc-b1f712334b83",
        "0876ef51-fee7-449d-ba1e-f2662c7e43c6",
        "08a3b009-0178-ee60-e357-e7ee5aea59c7",
        "0bbe0a49-3c63-49d3-ab4a-aa24198f03f7",
        "0c02a769-03f1-c4d7-85a5-db5dca505c49",
        "0d524e8d-4cfd-4db5-9f91-8b4bb5235a8e",
        "0da795d9-26d2-4f02-a019-0ec383363c88",
        "0db76759-6d22-4262-93f0-2f989ba2b58e",
        "0dc165fd-69bf-468a-aa04-a69377b6feb0",
        "0eb54047-acd9-4f26-8ffb-8cec713782d6",
        "0fb3f293-899e-458a-81cc-ad263dd89629",
        "10aedd06-621e-4b4f-a45c-5256573e0191",
        "10df9b5e-41b9-4dd1-bfe0-44177f9156e5",
        "12018f4f-3d10-999b-e4c4-86ec25be08a1",
        "123039b5-0fda-4744-9a17-d6b5d5d122b2",
        "1234abcd-1b53-4fd4-9835-2c2fa3935313",
        "1294987d-c97d-41d0-8fd8-cb6eab52d87b",
        "129d8c1e-a4d2-4bac-86ce-c7c2b2e37feb",
        "13e7d036-6903-821c-6018-962938929bf0",
        "14257785-9437-97fa-11ae-898cfb24302b",
        "148cdd60-97e8-426b-a7b9-141b7cb4bc2f",
        "148fec38-cb1b-46ad-84b9-41233d07d4d9",
        "14b28bdb-b83d-4f55-a516-44d4152f1f2b",
        "158f0a07-0a66-4a25-9e37-c43c49c8dd64",
        "1597605a-0faf-5860-eb74-462ae2e9fc21",
        "15be5f3c-e0a4-c0fa-fbff-8e50339b4b22",
        "16d0cf25-463d-4a20-8f18-d8d71edf92e3",
        "171f87ad-4ead-42fc-8f32-a3b18d451837",
        "17454550-1543-4068-bdaf-f3ed7cdd3d86",
        "18bf29b3-a844-e170-2826-4e95d0ba4dc9",
        "1964f651-15e7-4519-bd86-9a7c5335bfe4",
        "19beaa2a-a126-b4dd-6d35-617f6cc83fca",
        "19d45f8f-245c-852e-dbf9-d4aab4758b1f",
        "1a93e945-3675-aef6-075d-c661498e1046",
        "1aabfa0d-7585-f9f5-1d92-ecb40291d9f2",
        "1b4dd958-c202-47af-af97-99bfc98376a5",
        "1b8c5187-32a6-4a2f-8ca1-b0b7d6ce9e86",
        "1b94aa41-a51e-4cad-98fb-3a44447d5997",
        "1be22853-8ed1-4005-9907-ddad64cb1417",
        "1efe9592-f5ae-4167-97d7-63e973821fca",
        "1f39d16f-68b9-472b-a82d-cf7b5bed0430",
        "1f6d29f6-4edb-ea39-042b-de8f123ddd39",
        "1fde2073-a488-17e9-9534-5a3b23379b4b",
        "20dfc768-7850-4176-9707-b9bb52afb95a",
        "213974c8-ed9c-459f-9398-7cdaa3c28856",
        "22489c48-27d1-4e40-9420-4303ad9cffef",
        "22e93e92-4a31-b4cd-d640-3ef908430aa6",
        "23aa9cbe-c2fb-6a2f-6c97-885a6d48c4d1",
        "24d8af06-d441-40b4-a49c-311421aa9f58",
        "270c5ab3-31d0-461f-bf8d-55d739552d31",
        "276b1952-c364-852b-11e5-657f0fa34dc6",
        "293984cf-b551-461f-b22d-9659ebd09a4f",
        "2a54c352-7ca4-4bae-ad46-47ecd9595bd2",
        "2acc27c6-5fdb-405e-9080-cb66b850c8f5",
        "2acd365d-e8b5-4094-bce4-244b7c51d67c",
        "2af11142-942e-45c1-8ce8-d9d2df25aae9",
        "2b5eac39-9f50-4d8d-bc9b-1e1e07c5c37e",
        "2cbca084-4e80-4720-a7fe-dc8c3074e8ca",
        "2e41fe84-7173-4fe9-b257-61aa4679c3fe",
        "2e96bc2f-1972-e471-9e70-ae58d41e9d2a",
        "2ee9f31e-df58-4893-b3e7-66c0cd74183a",
        "2f77028c-f3a0-467c-9dd3-4d29d56ad460",
        "314a2614-24d3-496c-b9d6-e6cd3df4b6c2",
        "32755df6-aa2f-48d7-9ab7-92b8a80352ea",
        "3327646a-c325-417f-a3e3-36ae7119da69",
        "33557a7c-6dd6-4b46-9579-fc5273f07458",
        "33b66f53-738a-4200-8672-63c47a15144e",
        "33e515fe-354c-4016-a0f7-c4d6585aea61",
        "35b25be2-d08a-e340-45ed-f08a95d804fc",
        "35f45c95-27cf-4e52-891f-8390d1de5828",
        "36dff9ef-afde-40f5-b742-79a0bafcf6c2",
        "38500a53-575d-44b7-8f29-6cd534137438",
        "386452d3-8df0-4174-94cb-fee063b3084f",
        "38f4a461-1543-4089-854c-90e7edf37707",
        "39c63596-aa92-1b90-ee7c-628bee592cc0",
        "3a3c1a2a-8597-4d3a-981a-0a24a0ee9de4",
        "3a577f3e-2a57-4197-bc79-85007d5c8cd8",
        "3ef9848c-c2c8-4ff3-8b9c-4c8eb8ddfce6",
        "3f6368d4-6473-499d-80e3-2d03e6313ae6",
        "3f6c5689-6a05-4896-a6e0-c6f8a22a44c2",
        "407b6ad6-8e0b-40e7-9384-643520cae0ed",
        "42dbf883-9e4b-4f84-9da4-232b87c4b5e9",
        "43a3c88f-5bef-46c8-8e17-932159b3287d",
        "4440efc8-6c5c-4f65-8dea-9d0aa96790f3",
        "44a0a07f-23a2-49df-b8dc-a1b14c7c6a9d",
        "45cfc38d-3ffd-4088-bb15-e4d0e1e160fe",
        "45cfe080-ceb1-a91e-9743-71551ed24e94",
        "462b5f77-4a65-4287-885b-01a0f471743f",
        "47b11ec4-7950-43a1-b6b5-f051f812bd34",
        "48432aa1-f081-4de9-9e7e-e2e6a7d354bb",
        "48ae14cb-10de-4bd9-a005-5c25f498649b",
        "4a3d7cd3-f17c-637a-1ffc-614a01dd03cf",
        "4a993d7c-9d83-4d85-b5a9-7cce0b136378",
        "4c72c554-1573-4ce8-8bbf-7b2aab0bf297",
        "4dce8273-2f9d-4c20-91ab-9485b03b7d10",
        "4e13bb59-a859-45b5-ab5a-19363a34084e",
        "4ed62ae4-5072-f9e7-8d94-51c76c48159a",
        "4fb67663-9ab9-475d-b026-8c544cced439",
        "4ffc56f4-3fa7-49e2-adaa-e0c1960e612d",
        "51a4e6bd-5a95-4a41-8309-40f5640fdb8b",
        "51fd8bb1-0db4-bbf1-7e2b-cfcba7eb66a6",
        "52a9d0a7-efe1-4512-9716-394abd4e0ab1",
        "52f7826a-ace7-3107-dd0d-4875853c1576",
        "53572822-d3fc-4363-bfb9-248645841612",
        "53e0a3cb-3569-474a-8d7b-7fd06a8ec227",
        "550e890b-e652-4d22-8274-60b3bdb24c63",
        "56a6e81f-7413-4f72-9a1b-aaeeaa87c872",
        "58d6648d-32e8-4346-827c-4f288dd8ca24",
        "58d72d9d-0310-4792-9a3b-6dd111093cdb",
        "59a83512-d885-4f09-8e4f-c796c71c686e",
        "5a3d6cdd-8eb3-46d2-ba11-d24a0d47fe65",
        "5a659d57-117d-bb18-65f6-54e51da1bb9b",
        "5b8ddf04-be28-44ec-ab2c-a63a34d1de13",
        "5e4e9f04-9201-4fd9-8af6-a9539d13d8ec",
        "5f65e47f-7a00-4bf3-acae-90ee441ee876",
        "60a55165-9ccd-4536-81f6-e8dc6246d3d2",
        "6230537d-113a-42ec-9357-c08d01602787",
        "624b0218-0a0e-4b48-a961-33dbafdebb47",
        "661dd0c2-5d39-4cfb-ba57-59808643e36d",
        "66d3137a-c4da-4c8a-b6b8-e03f5dfba66e",
        "6747b02b-b6ac-4c2e-aeca-c2aa0438f58d",
        "67fc622b-4ce6-8c52-08ae-9f830036b757",
        "680a5388-28aa-44e8-88af-32e3598dc869",
        "684a5b6d-a270-61ce-306e-5cea400dc3a7",
        "69133b6b-695a-43eb-a763-221e19556755",
        "692343df-7e70-b082-7b0e-67f97146cea3",
        "69ad830b-d98c-b1cf-2158-9d69d38c7093",
        "6a2b1e70-bd4c-4163-86de-5243d7ac05ee",
        "6aa7a0df-192f-4dfa-bd61-f43db4843e7d",
        "6ac66a74-761f-4a59-928a-d373eea3f028",
        "6b51b7f7-cbed-75bf-8a02-43384bf47562",
        "6b86d069-b3c3-b4d7-47c7-e73ddf786a63",
        "6c27f068-4db9-6283-db1d-e4bdbd683a4b",
        "6c99f570-2ce7-46bc-8175-cde013df43bc",
        "6cd70072-c45c-4716-bf7b-b35c18e46e72",
        "6dcd6657-7a07-404a-b462-db76946f6a97",
        "6dcdcb36-ee1d-4507-ab15-093098330426",
        "6f33a917-418c-4608-b34f-4ff0e7be8637",
        "702b474d-698f-4029-9f9d-4782c626923e",
        "70f87e66-9b2d-4bfa-ae38-1d7d74837689",
        "7139a514-8349-c7a6-ce39-73ba2d8c48d9",
        "71992a2a-d168-42e0-b10e-6b45fa2ecddb",
        "720a3e77-0b9a-4fa9-98b6-ddf0fd7e32c1",
        "74aa92b7-9c42-4640-9b1b-8ab645c86a00",
        "74e7dcff-317f-9635-41d2-ead5019acc99",
        "75396512-3323-9be4-059d-32ecb113c3de",
        "75930197-b082-4f29-aff1-96d58cf5ea2a",
        "75c8c891-46d2-41fa-a81c-84e870a139a9",
        "7747ce74-9209-4fe4-8dd8-6cd74ac1c9ba",
        "78211c00-15a9-336e-17c4-0b48613dadf4",
        "78c5ab69-858a-43ca-a5ac-4ca6f9cdc30d",
        "7b2a234d-614b-562f-ac85-91b419688b59",
        "7c27d589-c7ed-47e1-8fe9-fe12ea81634a",
        "7c380315-6ad9-4fb2-8930-a8aeb1d6241b",
        "7c83695a-3fa9-4668-9080-85151f5ab7be",
        "7cdecd2c-a8b0-41cf-b0a4-528bd4d85f5a",
        "7e76e54f-7978-4d48-9ab9-a4da5b7c69a3",
        "7e9fbfe8-1234-435c-b114-424445c9be6f",
        "7f04fc0c-4a3d-5c7e-ce19-666cb871b510",
        "805651bc-6ecd-4c73-9b55-97a19d0582d0",
        "80efd6cb-dcee-491b-83a4-7956e9e058d5",
        "8109a740-abe9-453e-91fc-c25598de73d0",
        "814df446-7128-eff0-9177-fa52ac035b74",
        "8433e84a-8f5c-4b6c-9052-9b98757348ea",
        "84978654-5304-4b2a-81f6-022d18a8b676",
        "84b1a508-fc21-49da-979e-96894f1665df",
        "860d2d5d-7934-4ccb-a34a-577adf3022a6",
        "861bbc73-0a55-8d1d-efc6-e92d9e1176e0",
        "86ea1a79-29d3-4eac-a9f4-3541ace4e718",
        "87269ca9-dda6-448e-97ac-c5888b2a2d61",
        "87448ec1-55f6-3746-3f79-0f35beee76b4",
        "874b14bd-b49e-495a-88c6-46acb89b0a33",
        "885cd4f5-dfa0-4d68-bbfd-00f89fc2b69c",
        "8941d121-f740-35f6-952c-6561d2b38d36",
        "8962964c-a6d6-4c3d-918a-2777f7fbdca7",
        "8ad68a2f-c6b1-97b5-41b5-174359a33688",
        "8bc390da-9eb6-938d-25ed-44a35d9bcc9d",
        "8c3e93d3-0276-4d06-b20a-9a9f3012742c",
        "8d31f25f-31a9-4267-b817-20ee44f88069",
        "8e2b96ff-3de2-289b-b5c1-3b9921a3441e",
        "8ee30d6b-2c73-452a-b4ad-e4386cd6f7d0",
        "8fd46c9b-5ba1-4133-8a5d-dfc61e1195b1",
        "9017e82f-b7ac-4a06-8b9b-5858cb3d5113",
        "94208a8b-16e8-4e5b-abbd-4e81c9d02bee",
        "944611b9-0357-4272-a9ac-a97a65932599",
        "947a627a-532d-44f8-8e23-4f365a80a2ba",
        "95592ab0-ddc8-660d-67f3-6df1fadfe7ec",
        "961eb649-3ea9-f8c2-6595-88e9a3aeedeb",
        "96327a68-4aec-5e76-8f0e-d4670bc5a3a7",
        "96d733d8-6d43-4340-ba9a-c7bbdef18f62",
        "97172837-e5ea-45b2-af3b-cadbf428a6d9",
        "972a6579-f38f-c0b9-1b4b-a5bbeba3ab5b",
        "97b38421-f88c-4db0-b397-b2d81eff6630",
        "993cf5a8-a5c6-4dd6-ac68-fd8c5681d93e",
        "997839f4-48e4-49e4-9b15-628a7757765c",
        "99811474-2a6c-4d40-ac91-ae76c76e3258",
        "9b0d1cf7-8a3a-4c8b-8f9f-1c3e70e399d6",
        "9b7d740f-c271-4bfd-88fb-515680c33440",
        "9b828565-a0ed-61c2-6bf3-1afc99a9b2ca",
        "9d07b7e6-2986-4964-a76c-b2689604e212",
        "9d7196d1-2d7c-4316-820f-7374a4ddf250",
        "9db740c1-a220-46a9-a544-a0c021ec0ca5",
        "9ebff5d5-10c1-4fed-8c58-1954e27d3bfa",
        "a06456ed-afb7-4d16-86fd-0054e25268ed",
        "a092afdb-6f20-4b42-8d8f-423ac8d71a3f",
        "a0ad4f8c-f904-4b11-955d-e0044473c5fa",
        "a15a8fbc-22ac-41af-9039-2c9c4a7128e0",
        "a205074f-8049-48b3-903f-556f5e530ae3",
        "a25fccfd-854d-4c1a-9fae-aa0597a45e27",
        "a4255ba5-b07e-45ae-99ca-25e6c2079e3c",
        "a5ab10c5-424a-4818-9fba-ddca1eee531a",
        "a5f888e3-8cf4-4491-b2ba-b120e14eb7ce",
        "a67201dd-6df0-4838-8258-5abf26adc8f6",
        "a71bfb94-b9e8-473e-b0a5-9fafc92cdb05",
        "a77dd319-ffb5-4f88-bdf2-e98e59afc79f",
        "a8604ddc-7087-4752-b0b3-8fed1a5a37a6",
        "a8fd63ce-4600-43eb-af33-a6d5481f5930",
        "a9341235-9389-42f0-a0bf-9bfb57960d44",
        "a9a53f4f-26b6-3d68-33f3-2ec1f2452b5d",
        "aa395469-1687-78a7-bf76-f4614ef72977",
        "aae10e53-8403-3576-5d97-3b00f97332b2",
        "abb1f687-2d58-4197-8f5b-8882f05c04b8",
        "ad50b498-f90c-451f-886f-d0a169cc5002",
        "ae2b8ab9-f6b9-4531-ba04-44f00880dc18",
        "af560c4d-9c05-e073-b9f1-f7a94958ff25",
        "af849052-4299-0692-acc0-bffcbe9e440c",
        "afdf4c1a-e46b-4817-a5d6-4b9909f58e2a",
        "b020ff96-37bf-4a64-8bd5-2bfb3fdf3f87",
        "b1af52e4-e968-4e2b-b6d0-6736c9651f0a",
        "b2c74ac7-061e-4164-b272-ecb0940f5965",
        "b30897cc-2c2e-4677-a2a1-107ae982ff49",
        "b34f9fe7-80cd-6fb3-2c5b-951993746ca8",
        "b353f187-4cb4-4b2b-b502-472f45f32fd6",
        "b3efb46f-6d30-4201-98de-6492c1f8f10d",
        "b4704ab8-e8fd-4bb4-8096-d04b073ede2d",
        "b57f7a29-dcc8-43de-86fa-18d3f9d3764d",
        "b7316772-5c8f-421f-bed0-d86b0f128e25",
        "b7604066-ed76-45f9-a5c1-c97e4812dc55",
        "b8d89adf-9b67-4c44-8a08-5f40f5a5f1ab",
        "ba1f4576-9ace-4fa9-b0d6-311ad9f2f233",
        "ba975338-f956-41e7-a9f2-7614832d382d",
        "bbc3f0f1-85b7-4bcb-b474-0e02571eb5fa",
        "bbd14f11-6228-4588-82a4-517b8d77b23f",
        "bbd39b95-99d9-4b7e-b66b-8813081307c1",
        "bc303248-3d14-44c2-96a0-55f5c326b5fe",
        "bcfeb92b-fe93-4cea-adc6-e747055518e9",
        "bd109fe8-a2cf-415a-adcb-5e9f9fc1d3c0",
        "bdac9c7b-b9b8-f572-0450-f161c430861c",
        "bdb595a4-e148-41f9-98e8-68ec92d1932e",
        "be264018-593c-1162-bd5e-b74a39396652",
        "beb62be3-5e78-49bd-ac5f-099250ef3c7c",
        "c03eebb8-b373-453d-9555-83266c257c71",
        "c0576597-4910-48b5-9828-5b3a99190b82",
        "c0f5316d-5ac5-9218-b77a-b96e16ccfd66",
        "c1f5f212-7dda-4fb2-aa42-8178bfc8f189",
        "c249dc0e-9a17-423e-838a-d72719e8c5dd",
        "c2ab4bea-c663-3259-a4cd-03a8feb02825",
        "c2c90d64-38e2-e984-1457-7f4a98168c72",
        "c3c74c9e-e241-496c-be3f-57a2797aa91f",
        "c571b9b2-fe79-4785-8083-30b7b57a4f3d",
        "c5b83aed-f53d-5201-8ffb-1f9938de410a",
        "c6ac1f03-bd58-4421-9522-23cffb64d8e1",
        "c6b94711-f1f5-4e7e-9c89-c17ed4190969",
        "c8bbcb72-b778-48b4-882c-d8ce271995e5",
        "ca4e6a5a-3a9a-bad3-798a-d420a1d9bd6d",
        "ca98bba7-719e-48ee-e193-0b76766cdb07",
        "cbd1b299-b933-45bb-83a5-4061e515e826",
        "cc6d1865-7617-3cb2-cf7d-4cfc01ece1df",
        "cdc78c07-02b0-4af0-1cb2-cb7c672a8b0a",
        "cdcf4f71-60d3-540b-91e3-aa19792da364",
        "cdf51428-a41b-4735-ba23-39f3b7cde20c",
        "ce2768c3-a7c7-1bbf-22cd-f9db675a9807",
        "ceb9372d-60f6-4564-8033-a8b1ead4fa76",
        "cec4922b-1eb3-cb74-660b-ffad9b9ac642",
        "d1db3318-01ff-16de-29eb-28b344515626",
        "d374a732-e69b-41dc-bbc2-a7234e2270be",
        "d42d751d-682d-48f0-bc24-bb15b61ac4b8",
        "d5d090f1-7d5c-9b38-7344-0ede8343276d",
        "d6b4832b-5ad3-454c-ac5f-1543bd1462dc",
        "d74d2738-2485-4103-9919-69c7e63776ec",
        "d79a60ef-d490-484e-91ed-f45ceb0e7cfb",
        "d8326952-60bb-40fb-b33f-51e662708a88",
        "d89829c9-dadf-4ddc-87d6-fd746debd5d3",
        "d9823f54-3eaa-485b-a3b0-b9559c8e831f",
        "da4d47d5-b48b-4308-93bc-29d954424e76",
        "da6630fb-4286-4996-92a3-a43f5f26dd34",
        "db621e98-4a20-4942-b174-c455dc71dbae",
        "dbd0cb49-b563-45e7-9724-889e799fa648",
        "dc045941-8e65-437b-992b-1f0acd28bb6e",
        "dc791c8d-a74e-4b3e-b7f1-40793399ecd6",
        "dd65e838-4473-4fdb-b124-e09798e35f36",
        "dd93fbbf-e5ef-4c7c-886e-2bfef0958f45",
        "dea5192e-1bb3-101b-b70c-4646546f5e1e",
        "e070c4bf-afaf-413e-bc00-e476b89c5f3d",
        "e0ba1234-61da-46e3-a66d-fa0752b9df7d",
        "e10b1381-5f0a-47ff-8c7b-37bd13d7c974",
        "e27c5181-5005-4dc3-a449-89b726a3bf54",
        "e2f798b8-621a-4d46-99d7-1310e09eba26",
        "e2fa79e2-b3e0-11e9-a2a3-2a2ae2dbcce4",
        "e7ee30c4-bac9-2966-54bd-2023a4282872",
        "e8407fab-bf38-b0a4-79c1-068bbf82eca1",
        "e94a7421-fc27-7a4d-e9ba-2ba01384cacd",
        "e9a96e96-c68f-4604-b9ff-6b57ffb693da",
        "eb4f67d2-2440-4d58-bec7-6de73cc5ba75",
        "ebe970fe-9c27-4dd7-a165-1e943d565e10",
        "ec6fe20c-08d6-43da-ac18-84ac83756a88",
        "ed651749-cd37-4fd5-9897-01b416926745",
        "eedc2853-3369-4ede-8a75-68caf73e24df",
        "ef14bcc2-41a5-41f6-bca8-10764cfbdee0",
        "efe75f01-6fff-5d9d-08e6-092b98d3fb3f",
        "f0382960-6906-4b0d-add3-ed12690bff31",
        "f0fb2a7e-16d5-849f-be57-86db712e9bd0",
        "f0fd27eb-25aa-4335-0ba2-0720cccda9a4",
        "f11b27f2-8c49-5bb4-eff5-e1e5384bf95e",
        "f19ab7d9-5ff2-f8fd-ab3b-0bf95dcb6889",
        "f266acba-699d-4900-ae93-1bb488fd69df",
        "f606607c-ee34-445e-997e-49d7cb563fe0",
        "f62ef41c-2cdb-4f4e-9dc9-a391c579b0fb",
        "f67fb4ed-d481-44d7-91e5-efadf504f74a",
        "f6b0e473-eb23-c3be-fe61-2ae3e8309530",
        "f6e3ad9c-5d58-48ba-b06b-ebffba60dd18",
        "f738efb8-005f-680d-3d43-b3db762d6243",
        "f78c8e26-9c40-4a74-a091-f76aecb49099",
        "f892f705-a708-47b0-9de2-95a958c479c2",
        "f9f0eed0-f143-47bf-b856-671ea2eeed62",
        "fc84abc0-eee6-4758-8372-a7681965ca44",
        "feba5625-68c8-4b53-90b4-8a9de4f71e9e",
        "ffff0522-1e88-47fc-8382-2a80ba848f5d"
    ]


def authenticate(azure_application_secret, azure_application_id, azure_subscription_id):
    token_url = f"https://login.microsoftonline.com/{azure_subscription_id}/oauth2/v2.0/token"

    token_payload = {
        "grant_type": "client_credentials",
        "client_id": azure_application_id,
        "client_secret": azure_application_secret,
        "scope": "https://management.azure.com/.default"
    }
    print(azure_subscription_id, azure_application_secret, azure_application_id)
    token_resp = requests.post(token_url, data=token_payload)
    token_resp.raise_for_status()
    return {
        'Authorization': f"Bearer {token_resp.json()['access_token']}"
    }


def fetch_advisor_recommendations(headers):
    advisor_recommendations_url = "https://management.azure.com/providers/Microsoft.Advisor/metadata?api-version=2023-01-01"
    advisor_resp = requests.get(advisor_recommendations_url, headers=headers)

    response = advisor_resp.json()
    resp_list = []
    supported_values = []
    for each_resp in response['value']:
        supported_values.extend(each_resp['properties']['supportedValues'])


    for each_sup in supported_values:
        if each_sup['id'] not in RecommendationTypeGuid.IDS:
            resp_list.append({
                'ID': each_sup['id'],
                'displayName': each_sup['displayName']
            })

    df = pandas.DataFrame(resp_list)
    df.to_excel('advisor_recommendations.xlsx', index=False)


if __name__ == "__main__":
    auth_header = authenticate(args.azure_application_secret, args.azure_application_id, args.azure_subscription_id)
    fetch_advisor_recommendations(auth_header)
