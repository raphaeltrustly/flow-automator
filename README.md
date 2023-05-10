# FlowAutomator

This robot was created with the purpose of automating repetitive actions that tend to take time and be complex

## Installation

You'll need python installed and the libs below are required:

```bash
$ pip install selenium
$ pip install pipenv
```

## Usage

The main flow is centralized inside the `pages/payment_flow.py` on method `def pay(self):`

```python
    def pay(self):
        # will create a transaction with custom data
        self.__create_transaction(self.custom_data)
        # will create a transaction
        self.__create_transaction({})
        # will authenticate on admin console
        self.__authenticate()
        # will set the cutoff for next minute and get the file id created
        file_id = self.__update_cutoff()
        # will get the ptx for each transaction created
        ptx_list = self.__find_all_trx_ptx(file_id)
        # will run the ach processor
        self.__run_ach_processor()
        # will authenticate on crb simulator
        self.__authenticate_crb_simulator()
        # will simulate the send in crb
        self.__simulate_send_in_crb(ptx_list)
        self.__run_ach_processor()
        # will simulate the return in crb
        self.__simulate_nsf_in_crb(ptx_list)
        self.__run_ach_processor()
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.